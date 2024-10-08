# taken from https://code.activestate.com/recipes/578267-use-pil-to-make-a-contact-sheet-montage-of-images/

import argparse
from pathlib import Path
from datetime import datetime
from PIL import Image

def make_contact_sheet(fnames, grid_dim, photo_size, margins, padding):
    """\
    Make a contact sheet from a group of filenames:

    fnames       A list of names of the image files
    
    ncols        Number of columns in the contact sheet
    nrows        Number of rows in the contact sheet
    photow       The width of the photo thumbs in pixels
    photoh       The height of the photo thumbs in pixels

    marl         The left margin in pixels
    mart         The top margin in pixels
    marr         The right margin in pixels
    marb         The bottom margin in pixels

    padding      The padding between images in pixels

    returns a PIL image object.
    """

    # Calculate the size of the output image, based on the
    #  photo thumb sizes, margins, and padding

    marl = margins[0]
    marr = margins[1]
    mart = margins[2]
    marb = margins[3]

    marw = marl + marr
    marh = mart + marb

    ncols = grid_dim[0]
    nrows = grid_dim[1]

    photow = photo_size[0]
    photoh = photo_size[1]

    padw = (ncols - 1) * padding
    padh = (nrows - 1) * padding
    isize = (ncols * photow + marw + padw, nrows * photoh + marh + padh)

    # Create the new image. The background doesn't have to be white
    white = (255, 255, 255)
    inew = Image.new("RGB", isize, white)

    count = 0
    # Insert each thumb:
    for irow in range(nrows):
        for icol in range(ncols):
            left = marl + icol * (photow + padding)
            right = left + photow
            upper = mart + irow * (photoh + padding)
            lower = upper + photoh
            bbox = (left, upper, right, lower)
            try:
                # Read in an image and resize appropriately
                img = Image.open(fnames[count]).resize((photow, photoh))
            except:
                break
            inew.paste(img, bbox)
            count += 1
    return inew


def main():
    parser = argparse.ArgumentParser(description="Create a contact sheet from images in a directory.")
    parser.add_argument("directory", type=str, help="Directory containing the images")
    parser.add_argument("--cols", type=int, default=4, help="Number of columns in the contact sheet")
    parser.add_argument("--rows", type=int, default=4, help="Number of rows in the contact sheet")
    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.is_dir():
        raise ValueError(f"{directory} is not a valid directory")

    ncols, nrows = args.cols, args.rows
    files = list(directory.glob("*.JPG")) + list(directory.glob("*.jpg"))

    # Don't bother reading in files we aren't going to use
    if len(files) > ncols * nrows:
        files = files[: ncols * nrows]

    # These are all in terms of pixels:
    photow, photoh = 200, 150
    photo = (photow, photoh)

    margins = [5, 5, 5, 5]
    padding = 2
    grid_dim = (ncols, nrows)

    inew = make_contact_sheet(files, grid_dim, photo, margins, padding)
    
    # Generate output filename based on directory name and current date/time
    output_filename = f"contact_sheet_{directory.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    output_path = directory / output_filename
    
    inew.save(output_path)
    print(f"Contact sheet saved as: {output_path}")
    inew.show()

if __name__ == "__main__":
    main()

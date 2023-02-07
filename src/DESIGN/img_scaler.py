"""
Script used to scale images.
"""
import pygame as pg


def scale_multiply(surface: pg.Surface, scale_factor_x: float = 1, scale_factor_y: float = 1) -> pg.Surface:
    """
    Scales :param surface: of a :param scale_factor_x: on the x and :param scale_factor_y: on the y.
    :param surface: surface to scale
    :param scale_factor_x: width scale factor
    :param scale_factor_y: height scale factor
    :return: scaled surface
    """
    surf_area = pg.Surface.get_size(surface)
    new_size: tuple[int, int] = int(
        surf_area[0] * scale_factor_x), int(surf_area[1] * scale_factor_y)
    return pg.transform.scale(surface, new_size)


def scale(surface: pg.Surface, new_width: int, new_height: int) -> pg.Surface:
    """
    Scales :param surface: to :param new_width: and :param new_height:.
    :param surface: surface to scale
    :param new_width: scaled pixel width
    :param new_height: scaled pixel height
    :return: scaled surface
    """
    return pg.transform.scale(surface, (new_width, new_height))


def main() -> None:
    pg.init()
    pg.display.set_mode((100, 100))

    img_name = input("Enter image name: ")
    img_to_scale = pg.image.load(img_name).convert_alpha()
    mult_factor = int(input("Enter mult-factor: "))
    scaled_img = scale(img_to_scale, mult_factor, mult_factor)
    scaled_img_name = f"scaled_{img_name}"
    pg.image.save(scaled_img, scaled_img_name)
    input(f"{img_name} scaled by a factor of {mult_factor} and correctly saved as {scaled_img_name}")


if __name__ == "__main__":
    main()

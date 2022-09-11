from os import walk
import pygame


def import_folder(path):  # Get the generated list of all pictures in this folder
    surface_list = []
    for folder_name, sub_folder, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()  # Generate a faster picture format
            surface_list.append(image_surf)

    return surface_list
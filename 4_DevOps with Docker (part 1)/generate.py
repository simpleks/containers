import os

# Ścieżka do folderu głównego z podfolderami
image_folder = "images"
# Nazwa pliku README, który chcemy wygenerować
readme_filename = "README.md"


def generate_readme(image_folder, readme_filename):
    readme_content = ""

    # Iteracja po podfolderach w folderze głównym
    for chapter_name in sorted(os.listdir(image_folder)):
        chapter_path = os.path.join(image_folder, chapter_name)

        # Sprawdzamy, czy to jest folder
        if os.path.isdir(chapter_path):
            # Dodajemy nagłówek rozdziału
            readme_content += f"## {chapter_name}\n\n"

            # Pobieramy listę obrazów PNG w danym podfolderze
            images = sorted([img for img in os.listdir(chapter_path) if img.endswith('.png')])

            # Generujemy wpisy dla każdego obrazu
            for i, img_name in enumerate(images, start=1):
                img_path = os.path.join(image_folder, chapter_name, img_name)
                readme_content += f"{i}. Zrzut ekranu numer {i}:\n![{i}]({img_path})\n\n"

    # Zapisujemy treść do README.md
    with open(readme_filename, "w") as readme_file:
        readme_file.write(readme_content)

    print(f"Plik '{readme_filename}' został wygenerowany.")


# Wywołanie funkcji
generate_readme(image_folder, readme_filename)
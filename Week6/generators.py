import os
import string
import random
import pyautogui
import sys
from pygame import mixer


def chain(iterable_one, iterable_two):
    if type(iterable_two) != type(iterable_one):
        raise ValueError('Objects types must be equal!')

    for elem in iterable_one:
        yield elem

    for elem in iterable_two:
        yield elem


def compress(iterable, mask):
    for item in mask:
        if not isinstance(item, bool):
            raise ValueError('Object in mask is not bool!')

    for item, elem in zip(iterable, mask):
        if elem:
            yield item


def cycle(iterable):
    length = len(iterable)
    i = 0
    while i <= length:
        if i == length:
            i = 0
        yield iterable[i]
        i += 1


def book_reader(book_name):
    current_chapter = ''
    remove_first_empty_string = False
    all_book_directory_files = [filename for filename in os.listdir(book_name)]
    for filename in sorted(all_book_directory_files):
        with open(book_name + '/' + filename, 'r') as file:
            line = file.readline()
            while line:
                if line[0] == '#' and remove_first_empty_string is True:
                    yield current_chapter
                    current_chapter = ''
                current_chapter += line + ''
                remove_first_empty_string = True
                line = file.readline()
            if filename == sorted(all_book_directory_files)[-1]:
                yield current_chapter


def read_book(book_name):
    book = book_reader(book_name)
    print(next(book))
    for elem in book:
        choice = input('If you want to print next chapter press space and then enter:\n')
        while choice != ' ':
            choice = input('If you want to print next chapter press space and then enter:\n')
        print(elem)


def generate_random_word_with_random_length():
    length_of_word = random.randint(1, 10)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length_of_word))


def generate_book(chapters_count, chapters_length_range):
    os.mkdir('new_book')
    current_chapter_counter = 1
    with open('new_book/' + str(current_chapter_counter) + '.txt', 'a') as file:
        while current_chapter_counter <= chapters_count:
            file.write('#Chapter ' + str(current_chapter_counter) + '\n')
            current_words_counter = 0
            while current_words_counter <= chapters_length_range:
                new_word = generate_random_word_with_random_length()
                file.write(new_word + ' ')
                add_end_line = random.randint(0, 1)
                if add_end_line == 1:
                    file.write('\n')
                current_words_counter += 1
            file.write('\n')
            current_chapter_counter += 1


def get_coordinates_of_mouse():

    while True:
        x, y = pyautogui.position()
        if x == 0 and y == 0:
            beep_sound2()
        yield x, y


def beep_sound1():
    sys.stdout.write('\a')
    sys.stdout.flush()


def beep_sound2():
    mixer.init()
    alert = mixer.Sound('bell.wav')
    alert.set_volume(0.1)
    alert.play()


def beep_when_mouse_is_in_top_left_corner():
    coords = get_coordinates_of_mouse()
    for elem in coords:
        continue


def main():
    # print(list(chain(range(0, 4), range(4, 8))))
    # print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    # read_book('Book')
    # print(generate_random_word_with_random_length())
    # print(generate_random_word_with_random_length())
    # print(generate_random_word_with_random_length())
    # beep_sound()
    # generate_book(10000,1000)
    # print(next(get_coordinates_of_mouse()))
    # read_book('new_book')
    beep_when_mouse_is_in_top_left_corner()

if __name__ == '__main__':
    main()

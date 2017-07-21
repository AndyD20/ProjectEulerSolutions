#!/usr/bin/env python
import timeit

one_to_nineteen = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven'
    , 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def main():
    words = ""
    formatted_words = ""
    for i in range(1, 1001):
        tmp = int2word(i)
        words += tmp
        formatted_words += tmp + ", "

    print("Length was: " + str(len(words.replace(" ", ""))))
    print(formatted_words)


def int2word(i):

    if i < 20:
        word = "{0}".format(one_to_nineteen[i - 1])
    else:
        word = list(str(i))
        if len(word) == 2:
            if int(word[1]) == 0:
                word = "{0}".format(tens[int(word[0]) - 2])
            else:
                word = "{0} {1}".format(tens[int(word[0]) - 2], one_to_nineteen[int(word[1]) - 1])

        elif len(word) == 3:
            if int(word[1] + word[2]) < 20:

                if int(word[1]) == 0 and int(word[2]) == 0:
                    word = "{0} hundred".format(one_to_nineteen[int(word[0]) - 1])
                else:
                    word = "{0} hundred and {1}".format(one_to_nineteen[int(word[0]) - 1],
                                                        one_to_nineteen[int(word[1] + word[2]) - 1])
            else:
                if int(word[1]) == 0 and int(word[2]) == 0:
                    word = "{0} hundred".format(one_to_nineteen[int(word[0]) - 1])

                elif int(word[2]) == 0:

                    word = "{0} hundred and {1}".format(one_to_nineteen[int(word[0]) - 1],
                                                                tens[int(word[1]) - 2])
                else:
                    word = "{0} hundred and {1} {2}".format(one_to_nineteen[int(word[0]) - 1],
                                                                tens[int(word[1]) - 2],
                                                                one_to_nineteen[int(word[2]) - 1])

        elif len(word) == 4:
            word = "one thousand"
    return str(word)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")

class UnknownLanguage(object):
    """UnknownLanguage class contains 3 instance variables,
    being words_in_lex_order, dictionary and alphabets.

    words_in_lex_order is given as a variable at initialization time
    and is used to construct the dictionary and the list of alphabets.
    """

    def __init__(self, words_in_lex_order):
        self.words_in_lex_order = words_in_lex_order
        self.alphabets = self._find_alphabets()
        self.dictionary = self._build_dict()

    def _find_alphabets(self):
        return set([letter for word in self.words_in_lex_order
                    for letter in word])

    def _build_dict(self):
        """Build a directed graph that represents the
        dictionary of all words.
        """
        self.dictionary = dict()
        separated_words = list()
        first_letters = self._separate_first_letter(separated_words, self.words_in_lex_order)
        while separated_words:
            self._update_dictionary(first_letters)
            for i in range(len(separated_words)-1, -1, -1):
                remaining_word_tails = separated_words[i]
                separated_words.remove(remaining_word_tails)
                first_letters = self._separate_first_letter(separated_words, remaining_word_tails)
        return self.dictionary

    def _separate_first_letter(self, separated_words, remaining_word_tails):
        """Separate words in remaining_word_tails into a dictionary.

        Args:
            separated_words: the list containing separated_words, this is also
                             the list that should be updated.
            remaining_word_tails: a list containing word tails that
                                  have the same prefix

        Returns:
            first_letters: the unique first letters that occurred list of remaining_word_tails
            N.B. separated_words is updated as well
        """
        first_letters = list()
        prev_first_letter = ""
        curr_first_letter = ""
        for word in remaining_word_tails:
            if len(word) > 0:
                curr_first_letter = word[0]
                if prev_first_letter != curr_first_letter:
                    separated_words.append(list())
                    first_letters.append(curr_first_letter)
                separated_words[-1].append(word[1:])
            prev_first_letter = curr_first_letter
        return first_letters

    def _update_dictionary(self, first_letters):
        """Add edges according to the order in list first_letters.
           To make sure that the original order is obtained,
           set() operation is NOT used. """
        for index, value in enumerate(first_letters):
            if index == len(first_letters) - 1:
                break
            in_edge = value
            out_edge = first_letters[index + 1]
            if in_edge != out_edge:
                self._add_edge(in_edge, out_edge)

    def _add_edge(self, in_edge, out_edge):
        """Add an edge to the dictionary. """
        if in_edge not in self.dictionary:
            self.dictionary[in_edge] = set()
        self.dictionary[in_edge].add(out_edge)

    def _find_alphabets_with_no_in_edge(self):
        alph_with_in_edge = set([alph for key in self.dictionary.keys()
                                 for alph in self.dictionary[key]])
        return self.alphabets.difference(alph_with_in_edge)

    def _no_in_edge_to(self, in_edge, out_edge):
        for key in self.dictionary.keys():
            if key != in_edge and out_edge in self.dictionary[key]:
                return False
        return True

    def topological_sort(self):
        """Use topological sort to sort the dictionary into a list of
        alphabets in lexicographic order.
        """
        sorted_alphabets = list()
        alphabets_no_in_edge = self._find_alphabets_with_no_in_edge()
        while alphabets_no_in_edge:
            in_edge = alphabets_no_in_edge.pop()
            sorted_alphabets.append(in_edge)
            if in_edge not in self.dictionary:
                continue
            for out_edge in self.dictionary[in_edge]:
                if self._no_in_edge_to(in_edge, out_edge):
                    alphabets_no_in_edge.add(out_edge)
            del self.dictionary[in_edge]
        if self.dictionary:
            raise ValueError("The graph of the dictionary contains loop! ")
        else:
            return sorted_alphabets

#!/usr/bin/env python

# Copyright (c) 2018, Vanessa Sochat
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# * Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived from
#  this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from random import choice


class EventNamer:

    _descriptors = [
        "chunky",
        "buttery",
        "delicious",
        "scruptious",
        "dinosaur",
        "boopy",
        "lovely",
        "carniverous",
        "hanky",
        "loopy",
        "doopy",
        "astute",
        "gloopy",
        "outstanding",
        "stinky",
        "conspicuous",
        "fugly",
        "frigid",
        "angry",
        "adorable",
        "sticky",
        "moolicious",
        "cowy",
        "spicy",
        "grated",
        "crusty",
        "stanky",
        "blank",
        "bumfuzzled",
        "fuzzy",
        "hairy",
        "peachy",
        "tart",
        "creamy",
        "arid",
        "strawberry",
        "butterscotch",
        "wobbly",
        "persnickety",
        "nerdy",
        "dirty",
        "placid",
        "bloated",
        "swampy",
        "pusheena",
        "hello",
        "goodbye",
        "milky",
        "purple",
        "rainbow",
        "bricky",
        "muffled",
        "anxious",
        "misunderstood",
        "eccentric",
        "quirky",
        "lovable",
        "reclusive",
        "faux",
        "evasive",
        "confused",
        "crunchy",
        "expensive",
        "ornery",
        "fat",
        "phat",
        "joyous",
        "expressive",
        "psycho",
        "chocolate",
        "salted",
        "gassy",
        "red",
        "blue",
    ]

    _nouns = [
        "squidward",
        "hippo",
        "butter",
        "animal",
        "peas",
        "lettuce",
        "carrot",
        "onion",
        "peanut",
        "cupcake",
        "muffin",
        "buttface",
        "leopard",
        "parrot",
        "parsnip",
        "poodle",
        "itch",
        "punk",
        "kerfuffle",
        "soup",
        "noodle",
        "avocado",
        "peanut-butter",
        "latke",
        "milkshake",
        "banana",
        "lizard",
        "lemur",
        "lentil",
        "bits",
        "house",
        "leader",
        "toaster",
        "signal",
        "pancake",
        "kitty",
        "cat",
        "cattywampus",
        "poo",
        "malarkey",
        "general",
        "rabbit",
        "chair",
        "staircase",
        "underoos",
        "snack",
        "lamp",
        "eagle",
        "hobbit",
        "diablo",
        "earthworm",
        "pot",
        "plant",
        "leg",
        "arm",
        "bike",
        "citrus",
        "dog",
        "puppy",
        "blackbean",
        "ricecake",
        "gato",
        "nalgas",
        "lemon",
        "caramel",
        "fudge",
        "cherry",
        "sundae",
        "truffle",
        "cinnamonbun",
        "pastry",
        "egg",
        "omelette",
        "fork",
        "knife",
        "spoon",
        "salad",
        "train",
        "car",
        "motorcycle",
        "bicycle",
        "platanos",
        "mango",
        "taco",
        "pedo",
        "nunchucks",
        "destiny",
        "hope",
        "despacito",
        "frito",
        "chip",
    ]

    _events = [
        "triathlon",
        "blessing",
        "awakening",
        "opening",
        "closing",
        "stoning",
        "dance",
        "festival",
        "study-session",
        "fishing-trip",
        "fair",
        "movie",
        "homework",
        "apocalypse",
        "reading",
        "dinner",
        "breakfast",
        "wedding",
        "airing",
        "training",
        "circus",
        "rodeo",
        "trick-or-treating",
        "speech",
        "wedding",
        "seminar",
        "knighting",
        "poetry-slam",
        "shopping",
        "eating",
        "burping",
        "swimming",
        "egging",
        "tp-ing",
        "chastizing",
        "glorifying",
        "pooping",
        "burping",
        "snoring",
        "sleeping",
        "hunt",
        "hiding",
        "celebration",
        "decorating",
        "cooking",
        "sneezing",
        "hackathon",
        "masquerade",
        "unmasking",
        "unveiling",
        "wondering",
        "skiing",
        "barbecue",
        "roasting",
        "event",
        "ball",
        "",
    ]

    def generate(self, delim="-", length=4, chars="0123456789"):
        """
        Generate a robot name. Inspiration from Haikunator, but much more
                 poorly implemented ;)

        Parameters
        ==========
        delim: Delimiter
        length: TokenLength
        chars: TokenChars
        """

        descriptor = self._select(self._descriptors)
        noun = self._select(self._nouns)
        event = self._select(self._events)
        numbers = "".join((self._select(chars) for _ in range(length)))
        return delim.join([descriptor, noun, event, numbers])

    def _select(self, select_from):
        """ select an element from a list using random.choice
        
            Parameters
            ==========
            should be a list of things to select from
        """
        if len(select_from) <= 0:
            return ""

        return choice(select_from)


def main():
    bot = RobotNamer()
    print(bot.generate())


if __name__ == "__main__":
    main()

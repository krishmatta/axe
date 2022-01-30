# axe &middot; ![Python Application](https://github.com/krishxmatta/axe/actions/workflows/python-app.yml/badge.svg)

axe is a command line tool that provides information from any Wikipedia page straight to your terminal. It can be used to either provide information from a specified page, or to provide information from a random page.

## Installation
To install axe,
1. Clone the repository with `git clone https://github.com/krishxmatta/axe.git`
2. Enter the repository with `cd axe`
3. Install with `python setup.py install`

## Usage
axe has two main functionalities: querying information from a specified Wikipedia page, and querying information from a random Wikipedia page. In either case, axe will print out the first paragraph found in the Wikipedia page.

To get information from a specific page, use the `search` subcommand followed by the title of the page you want to query: `axe search <page-title>`.

To get information from a random page, use the `random` subcommand: `axe random`.

## Examples

### `axe search`
```console
$ axe search fish
1) Fish
2) One Fish, Two Fish, Red Fish, Blue Fish
3) Will Fish
4) Big Fish
5) Fish farming
6) Albert Fish
7) Fish fin
8) Cusk (fish)
9) Fish and chips
Please enter the corresponding number of the article you want to choose: 
$ 1
Fish are aquatic, craniate, gill-bearing animals that lack limbs with digits. Included in this definition are the living hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups. Around 99% of living fish species are ray-finned fish, belonging to the class Actinopterygii, with over 95% belonging to the teleost subgrouping.
```

### `axe random`
```console
$ axe random
Page Title: Harvest Threshing
Le Dépiquage des Moissons, also known as Harvest Threshing, and The Harvesters, is an immense oil painting created in 1912 by the French artist, theorist and writer Albert Gleizes (1881–1953). It was first revealed to the general public at the Salon de la Section d'Or, Galerie La Boétie in Paris, October 1912 (no. 43). This work, along with La Ville de Paris (City of Paris) by Robert Delaunay, is the largest and most ambitious Cubist painting undertaken during the pre-War Cubist period. Formerly in the collection of the Solomon R. Guggenheim Museum in New York, this monumental painting by Gleizes is exhibited at the National Museum of Western Art, in Tokyo, Japan.
```

# Search Application
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains a search application implemented in Python. The application allows users to search for specific terms within a collection of text files and retrieve relevant results. It provides different search implementations, including linear search, index-based search, and hash table-based search, offering flexibility and efficiency in finding matching documents.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Search Implementations](#search-implementations)
- [File Descriptions](#file-descriptions)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The search application enables users to search for specific terms within a collection of text files. It employs different search algorithms to provide efficient and accurate results. The available search implementations include:

1. **Linear Search**: Performs a linear search through each file in the collection to find matching documents.
2. **Index-Based Search**: Builds an index of words to document IDs and utilizes this index to search for matching documents.
3. **Hash Table-Based Search**: Utilizes a hash table data structure to create an index and perform efficient searches based on the index.

The application supports both command-line usage and an interactive mode where users can enter search terms and view the results in an HTML format.

## Installation

To use this search application, follow these steps:

1. Clone the repository:

   ```bash
   $ git clone https://github.com/wangyuhsin/search-application.git
   ```

2. Install the required dependencies. The application requires Python 3 and the following libraries:

   - `os`
   - `re`
   - `string`
   - `collections`
   - `webbrowser`


3. Configure the application by specifying the search implementation and the root directory containing the text files to be searched. This can be done by modifying the `search.py` file.

4. The search application is now ready to use.

## Usage

To use the search application, follow these steps:

1. Open a command-line interface.

2. Navigate to the directory where the search application is located.

3. Execute the following command, replacing `<search-implementation>` and `<root-directory>` with your desired search implementation and root directory:

   ```bash
   $ python search.py <search-implementation> <root-directory>
   ```

   Replace `<search-implementation>` with one of the following options:
   - `linear` for linear search
   - `index` for index-based search
   - `myhtable` for hash table-based search

   Replace `<root-directory>` with the path to the directory containing the text files to be searched.
   
   For example:
   ```bash
   $ python search.py myhtable ~/data/slate
   ```

4. Follow the prompts to enter search terms and view the results.

## Search Implementations

### 1. Linear Search

The linear search implementation performs a simple search through each file in the collection. It matches the search terms with the words in the files and returns the documents that contain all the search terms. This implementation is straightforward but may be slower for larger collections.

### 2. Index-Based Search

The index-based search implementation builds an index from words to document IDs. It creates a dictionary that maps each word to a set of document IDs that contain that word. This index allows for efficient searching by quickly finding the relevant documents based on the search terms. This implementation is more efficient than linear search for large collections.

### 3. Hash Table-Based Search

The hash table-based search implementation utilizes a hash table data structure to build the index. It employs a custom hash table implementation that handles collisions using open hashing. This implementation provides efficient search capabilities by distributing the keys evenly across the hash table, reducing collisions and improving search performance.

## File Descriptions

The repository includes the following files: 
- `words.py`: Contains utility functions for processing text, including extracting words from a string, normalizing them, and generating search results.
- `linear_search.py`: Implements a linear search algorithm to find files that contain all the specified search terms.
- `index_search.py`: Implements an indexed search algorithm using a dictionary-based index to efficiently retrieve files containing all the search terms.
- `hash_table.py`: Defines a hashtable data structure as a list of lists with open hashing. It includes functions for creating the hashtable, computing hashcodes, and performing operations like inserting and retrieving key-value pairs.
- `myhtable_search.py`: Uses the hashtable implementation from `htable.py` to build an index and perform search operations.
- `search.py`: Provides a command-line interface for executing the search algorithms. It accepts the search type (linear, index, or myhtable) and the root directory to search in.

## License

The search application is released under the MIT License. You can find the details in the `LICENSE` file. Feel free to use and modify the search application according to your needs. Happy searching!

## Acknowledgments

The initial codebase and project structure is adapted from the MSDS 692 course materials provided by the University of San Francisco (USFCA-MSDS). Special thanks to the course instructors for the inspiration.

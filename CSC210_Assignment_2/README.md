# Assignment 2

This assignment is about testing the performance of linear search versus binary search. Please only modify the files that are indicated as being okay to modify.

The goal of this assignment is to write both search algorithms and to then test them. In addition, there are some written questions for you to answer.

## Basic Instructions

1. Create your own **private** repository from this repo by hitting the "Use this template" button at the top of the page
2. Add me (@davecom) as a collaborator on your **private** repository.
3. Implement the missing parts where it says "YOUR CODE HERE"
4. Test it on your local computer by following the build directions below
5. Push your code to GitHub. Every push will be automatically tested through a GitHub Action. You will know your code is correct when you see a green check mark next to the commit.
6. Answer all of the questions in `questions.txt` in your own file `answers.txt`.
7. Submit the URL to your private repository on Canvas. Submit even if you are not passing all tests so you can get partial credit.

## Specific Files

@files you should modify

- `README.md` this file
- `LICENSE` MIT License
- `experiment.py`@ Runs time trials of both algorithms
- `search.py`@ Linear search and binary search implementations
- `main.py` the main file that calls the functions to read the data and make the charts
- `tests.py` the unit tests to prove your code works

## Standard Library Restrictions

Please do not use the standard library at all for implementing the functions `linear_search()` and `binary_search()`. For the other functions, you can use the standard library as much as you want.

## Running

You will need Matplotlib installed to run the program. You can install it using:

```
pip install matplotlib
```

On some systems `pip` might be `pip3`. Running the program is as simple as:

```
python main.py
```

On some systems `python` might be `python3`.

## Testing

You can run all of the unit tests in the current directory by running:

```
python -m unittest discover
```

You can also run tests.py directly:

```
python tests.py
```

## Checklist for Submission

- [ ] Did you add me (@davecom) as a collaborator on the repository?
- [ ] Did you replace every area that said "YOUR CODE HERE" with your code?
- [ ] Did you ensure you are passing all of the unit tests? Do you see a green check mark on GitHub?
- [ ] Did you cite all sources, especially any place that you copied code from? Put code citations right next to where you inserted them.
- [ ] Did you add sufficient comments?
- [ ] Did you double check your code for good style?
- [ ] Did you put your name below mine at the top of any files you modified and any other appropriate places?
- [ ] Did you submit the URL to your repository on Canvas?
- [ ] Did you remember to include your `answers.txt` file with answers to every question?

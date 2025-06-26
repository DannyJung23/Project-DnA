# Project-DnA
This repo is my journal to document all the Data Structures and Algorithms concepts and their implementation I learned while solving programming problems and interview questions.

The solutions to the problems are grouped under their respective subtopic and concepts, focusing on repeatedly applying the common patterns.

The problems I solved are from <a href="https://leetcode.com/"> LeetCode.

<hr>

## How I solve problems:
```python
def solve_problem(problem):
  understand(problem)
  get_intuition(problem)
  analyse(problem)
  
  if is_easy_enough(problem):
    approach = brainstorm(problem)
    return implement_into_code(approach)
  
  while not is_solved(problem):
    approach = brainstorm(problem)
    design = draw_diagram(approach)
    initial_solution = implement_into_code(design)
    final_solution = optimise(initial_solution, edge_cases=True)
  
    if test(final_solution):
      break
  
  return final_solution
```

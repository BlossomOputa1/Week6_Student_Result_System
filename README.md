# Week 6 Student Result System

## Project overview and architecture

This Python project validates student and assessment data, calculates course
results, assigns grades and grade points, and calculates a credit-weighted GPA.
Responsibilities are divided by purpose:

- `main.py` demonstrates the application by generating a student result and
  calculating a GPA.
- `validation.py` validates student identity fields and assessment scores
  against their allowed ranges.
- `grading.py` maps a total score to a grade and grade point using the defined
  grade boundaries.
- `result_module.py` coordinates validation, score aggregation, result
  generation, and GPA calculation.
- `test_grading.py` tests grade and grade-point boundaries, endpoints, and
  invalid inputs.
- `test_result_module.py` tests score totals, generated results, and weighted
  GPA behavior, including invalid inputs.

## Setup, execution, and testing

Run these commands from the project directory with Python installed:

```text
python main.py
python -m unittest -v
```

The test command runs the complete `unittest` suite and reports each test.

## Code review: original routine (Step 11)

The original `def x(a, b, c, n)` routine has several concrete weaknesses:

1. **Opaque naming:** `x`, `a`, `b`, `c`, `n`, `t`, and `g` do not communicate
   the purpose or meaning of the function's inputs and intermediate values.
2. **Mixed responsibilities:** it adds scores, assigns a grade, prints output,
   and returns a value in one routine.
3. **Incomplete grade scale:** it handles only A, B, C, and F; it has no D or E
   grades and no 45- or 40-point boundaries.
4. **No input validation:** it accepts scores without checking types, valid
   ranges, or whether each assessment stays within its maximum.
5. **No total-range validation:** invalid or excessive totals can be assigned a
   grade rather than rejected.
6. **Hard-coded policy values:** grade thresholds and grade labels are embedded
   in conditional logic, making grading policy harder to inspect or change.
7. **Output side effect:** printing is coupled to the calculation, which makes
   reuse and automated testing less straightforward.
8. **Limited return value:** callers receive only the total, not the assigned
   grade or other structured result details.

The refactored design separates validation, grading, result composition, and
the demonstration entry point. Each module has a clearer responsibility and
the functions can be tested independently. Explicit function arguments make
dependencies visible, while returning structured results instead of printing
inside calculations improves reuse and testability.

## Practical reflection

1. **Why separate validation from result calculation?** Validation enforces
   input rules in one place before calculations proceed. This avoids
   duplicating checks and keeps calculation routines focused on their results.
2. **Which routines demonstrate functional cohesion?** `validate_student` and
   `validate_score` each validate a specific kind of input; `calculate_grade`
   and `calculate_grade_point` each map a score to one outcome;
   `calculate_total_score` only totals assessment scores; and `calculate_gpa`
   only computes a weighted GPA.
3. **How are dependencies made explicit?** Functions receive the values they
   use as parameters, and `result_module.py` imports the validation and grading
   functions it depends on.
4. **What happens when a score exceeds its maximum?** `validate_score` raises
   `ValueError`, so the invalid score is rejected before a total or result is
   produced.
5. **Which tests verify grade boundaries?** `test_grading.py` checks the
   transitions at 39/40, 44/45, 49/50, 59/60, and 69/70 for both grade and
   grade-point calculations, along with valid endpoints and invalid inputs.
6. **How do tests help preserve behaviour during refactoring?** They capture
   expected outputs, boundaries, and failure cases, so later changes can be
   checked against the established behavior.
7. **What further controls are needed before real institutional deployment?**
   Add institution-approved grading rules and policy review, secure
   authentication and role-based access, privacy safeguards and audit logs,
   durable backups, operational monitoring, and independent validation against
   real academic records before production use.
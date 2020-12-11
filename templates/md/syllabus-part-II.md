---
title: Course Syllabus Part II
subtitle: {{ subject }} {{ course_number }} - {{ title }}
---

Course Syllabus Part II\
{{ subject }} {{ course_number }} - {{ title }}\
{{ credit_hours }} Credit Hours

## Course Resources

### Course Text(s)

{% for textbook in textbooks %}
*{{ textbook.title }}{% if textbook.edition %} ({{ textbook.edition }}){% endif %}*\
{% if textbook.author %}{{ textbook.author }}{% endif %}{% if textbook.authors %}{{ textbook.authors| join(' & ') }}{% endif %}\
{{ textbook.publisher }}\
**ISBN-13:** {{ textbook.isbn13 }}\
**ISBN-10:** {{ textbook.isbn10 }}
{% endfor %}

### Required Resources

In this course, you will need to be able to:

{% for resource in required_resources %}- {{ resource }}
{% endfor %}

---

## Course Schedule

{{ weekly_schedule_table }}

## Course Activities

In this section of the syllabus, I will describe what we will be doing in each of the activities for each week. Specifically, I will be describing your deliverables – those items you need to submit at or before the deadline. You can find more detail on grading criteria for each category by viewing its detailed rubric.

### Exercises

You will be assigned an exercise or series of exercises based on the weekly topic to complete and submit to the assignment link. These are not group assignments to complete and should be done on your own. However, if you have questions about a specific exercise, you are encouraged to use the discussion board to discuss with your classmates, without completing the assignment together.

### Discussion

Each week, you will be making discussion posts in the specified forums. Each post must be a minimum of 250 words and contain at least one credible source. These responses should be “substantive” which means more than, “Neat!” or “Good job!” They should also not contain jargon or be a post that boils down to you reposting the same thing you’re commenting on in a different way.

---

## Grade and Point Breakdown

{{ grade_breakdown_table }}

---

## Late Work

Late work is not accepted unless arrangements are made with the instructor for very special, unavoidable circumstances. If you do not alert the professor before or shortly after something that will make you late, the chances of special arrangements are much lower. If in doubt, please email as soon as possible.

## Participation

Students are expected to login often and contribute to the class on a regular basis, including posting to the discussion board, submitting assignments, and participating in group activities as required. If you have specific participation requirements related to your educational funding or student status, you are expected to monitor your own participation to ensure you are in compliance with those requirements.

## Expectations for Students

*  Students should expect to spend approximately 10-15 hours per week to complete the activities and assignments in this course.
*  Students will log in as often as needed to complete their assignments and progress through the course.
*  Students will treat their classmates and the instructor with respect and courtesy.
*  Students are responsible for keeping current with the reading assignments and coming to class prepared to discuss the work assigned.
*  Students are responsible for knowing what assignments are due and when.
*  Students will submit only their own work and will not commit plagiarism or other acts of academic dishonesty.
*  Students will contact the instructor as soon as personal problems arise that may affect the student’s ability to complete assignments on time.

## Expectations for Faculty

*  The instructor will treat all students with respect and courtesy.
*  The instructor will make grading criteria clear and follow the criteria scrupulously in evaluating student work.
*  The instructor will provide feedback about student work within 6 days of due dates (or 24 hours prior to the next due date)—feedback that helps the student learn and improve.
*  The instructor will respond to all student messages within 48 hours.

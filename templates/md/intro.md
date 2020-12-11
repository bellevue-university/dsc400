# Contents of the Week

- Introduction
- Readings
- Supplemental Readings
- {{ lesson_number }}.1 Discussion: {{ discussion.title }}
- {{ lesson_number }}.2 Programming Exercise: {{ exercise.title }}

# Objectives/Topics

{% for objective in objectives %}- {{ objective }}
{% endfor %}
{% if resources %}# Weekly Resources

{% for resource in resources %}- {{ resource }}
{% endfor %}{% endif %}
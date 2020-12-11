import os
from pathlib import Path

import yaml
from pytablewriter import MarkdownTableWriter
from jinja2 import Environment, FileSystemLoader, select_autoescape

current_dir = Path(Path(__file__).parent).absolute()
templates_dir = current_dir.joinpath('templates')
lessons_directory = current_dir.joinpath('lessons')
build_directory = current_dir.joinpath('_build')
course_yaml = current_dir.joinpath('course.yaml')

env = Environment(
    loader=FileSystemLoader(str(templates_dir)),
    autoescape=select_autoescape(['html', 'xml'])
)


def read_lessons():
    lesson_files = [
        Path(entry.path)
        for entry in os.scandir(lessons_directory)
        if entry.name.endswith('.yaml') or entry.name.endswith('.yml')
    ]
    lesson_files.sort()

    lessons = []
    for lesson_path in lesson_files:
        with open(lesson_path) as f:
            lesson = yaml.load(f, Loader=yaml.CLoader)
        lessons.append(lesson)

    return lessons


def build_lesson(lesson):
    lesson_number = lesson['lesson_number']
    output_directory = build_directory.joinpath('md', 'week{:02d}'.format(lesson_number))
    output_directory.mkdir(parents=True, exist_ok=True)

    templates = [
        'discussion-board.md',
        'intro.md',
        'programming-exercise.md',
        'readings.md',
        'supplemental-readings.md'
    ]

    for template_name in templates:
        template = env.get_template('md/{}'.format(template_name))
        content = template.render(**lesson)
        output_path = output_directory.joinpath(template_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)


def create_weekly_schedule_table(lessons):
    value_matrix = [
        (lesson['lesson_number'], lesson['title'], '<br>'.join(lesson['readings']))
        for lesson in lessons
    ]
    writer = MarkdownTableWriter(
        headers=["Week", "Topic", "Assigned Reading"],
        value_matrix=value_matrix
    )
    return writer.dumps()


def create_grade_breakdown_table(context):
    grade_breakdown = context['grade_breakdown']

    total_points = 0

    for entry in grade_breakdown:
        point_value = entry['point_value']
        number_of_times = entry['number_of_times']
        total = point_value * number_of_times
        total_points += total

    value_matrix = []

    for entry in grade_breakdown:
        component = entry['component']
        point_value = entry['point_value']
        number_of_times = entry['number_of_times']
        total = point_value * number_of_times
        percentage = round(total/total_points * 100.0, 1)

        value_matrix.append([
            component, percentage, point_value, number_of_times, total
        ])

    value_matrix.append([
        "Total", 100.0, "", "", total_points
    ])

    writer = MarkdownTableWriter(
        headers=["Component", "Percentage", "Point Value", "Number of Times", "Total"],
        value_matrix=value_matrix
    )

    return writer.dumps()


def build_syllabus(lessons):
    with open(course_yaml) as f:
        context = yaml.load(f, Loader=yaml.CLoader)

    output_directory = build_directory.joinpath('md')
    output_directory.mkdir(parents=True, exist_ok=True)
    template_name = 'syllabus-part-II.md'
    context['weekly_schedule_table'] = create_weekly_schedule_table(lessons)
    context['grade_breakdown_table'] = create_grade_breakdown_table(context)
    template = env.get_template('md/{}'.format(template_name))
    output_path = output_directory.joinpath(template_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template.render(**context))


def main():
    lessons = read_lessons()
    build_syllabus(lessons)
    for lesson in lessons:
        build_lesson(lesson)


if __name__ == '__main__':
    main()

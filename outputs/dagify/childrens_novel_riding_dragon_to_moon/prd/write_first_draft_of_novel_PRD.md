# write_first_draft_of_novel PRD

## Description
Generates the initial narrative draft of a children's novel featuring a protagonist and dragon journeying to the moon, integrating character profiles, landing sequence, and plot twists into chapter structure and key events.


## Conceptual Info

The node composes a complete first draft of a children's novel by weaving together character details, a moon‑landing journey, and narrative twists into a structured chapter format.

## Docstring

### Summary
Generate a first‑draft novel from character profiles, landing sequence, and plot twists.

### Parameters

- **protagonist_profile** (dict): Dictionary containing protagonist_name, age, background, strengths, weaknesses, motivations, emotions.
- **dragon_profile** (dict): Dictionary containing dragon_name, dragon_age, dragon_personality_traits, dragon_skills, dragon_habits, dragon_strengths, dragon_weaknesses, dragon_motivations.
- **moon_sequence** (dict): Dictionary containing moon_landing_sequence, preparation_steps, flight_details, lunar_exploration_plan, landing_site_coordinates, sequence_completion_status.
- **plot_twists** (dict): Dictionary containing plot_twist_descriptions, obstacle_types, conflict_resolution_outcomes, turning_point_count, protagonist_growth_description.

### Returns

dict: A dictionary with keys novel_title, protagonist_name, dragon_name, chapter_titles, chapter_summaries, key_events, theme, and word_count.

### Raises

- ValueError: Raised if any required input field is missing or empty.
- TypeError: Raised if inputs do not match expected structure or types.

### Examples

```python
>>> draft = write_first_draft_of_novel(protagonist_profile=protagonist,
...                                  dragon_profile=dragon,
...                                  moon_sequence=moon_seq,
...                                  plot_twists=twists)
{'novel_title': 'Starlight Riders', 'protagonist_name': 'Luna', 'dragon_name': 'Eclipse', ...}
```

```python
>>> print(draft['theme'])
'Bravery and friendship can conquer even the sky's limits.'
```

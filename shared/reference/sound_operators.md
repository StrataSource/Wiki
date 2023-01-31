---
layout: default
title: SOS Operator List
parent: Reference
---

# Sound Operator Stack System (SOS) Operator List

This document contains a list of available sound stack operators in Chaos.

# Operator `sys_block_entries`

## Inputs

- `input_execute`
- `input_duration`
- `input_active`

# Operator `set_convar`

## Inputs

- `input_execute`
- `input`

# Operator `get_convar`

## Inputs

- `input_execute`

## Outputs

- `output`

# Operator `get_dashboard`

## Inputs

- `input_execute`

## Outputs

- `output`

# Operator `math_delta`

## Inputs

- `input_execute`
- `input`

## Outputs

- `output`

# Operator `calc_distant_dsp`

## Inputs

- `input_execute`
- `input_distance`
- `input_level`

## Outputs

- `output`

# Operator `get_entry_time`

## Inputs

- `input_execute`

## Outputs

- `output_entry_elapsed`
- `output_sound_elapsed`
- `output_stop_elapsed`
- `output_sound_duration`

# Operator `game_entity_info`

## Inputs

- `input_execute`
- `input_entity_index`

## Outputs

- `output_position`
- `output_position_x`
- `output_position_y`
- `output_position_z`
- `output_angles`
- `output_velocity_vector`
- `output_velocity_vector_x`
- `output_velocity_vector_y`
- `output_velocity_vector_z`
- `output_velocity`
- `output_velocity_xy`

# Operator `calc_falloff`

## Inputs

- `input_execute`
- `input_distance`
- `input_level`

## Outputs

- `output`

# Operator `calc_falloff_curve`

## Inputs

- `input_execute`
- `input_distance`
- `input_curve_amount`
- `input_min`
- `input_max`
- `input_atten`
- `input_volume_min`

## Outputs

- `output`

# Operator `math_float_filter`

## Inputs

- `input_execute`
- `input`
- `input_max_velocity`

## Outputs

- `output`

# Operator `iterate_merge_speakers`

## Inputs

- `input_execute`
- `input_max_iterations`
- `input`

## Outputs

- `output_index`
- `output`

# Operator `get_map_name`

## Inputs

- `input_execute`

## Outputs

- `output`

# Operator `math_func1`

## Inputs

- `input_execute`
- `input1`

## Outputs

- `output`

# Operator `math_float`

## Inputs

- `input_execute`
- `input1`
- `input2`

## Outputs

- `output`

# Operator `math_vec3`

## Inputs

- `input_execute`
- `input1`
- `input2`

## Outputs

- `output`

# Operator `math_speakers`

## Inputs

- `input_execute`
- `input1`
- `input2`

## Outputs

- `output`

# Operator `math_float_accumulate12`

## Inputs

- `input_execute`
- `input1`
- `input2`
- `input3`
- `input4`
- `input5`
- `input6`
- `input7`
- `input8`
- `input9`
- `input10`
- `input11`
- `input12`

## Outputs

- `output`

# Operator `calc_source_distance`

## Inputs

- `input_execute`
- `input_position`

## Outputs

- `output`

# Operator `calc_angles_facing`

## Inputs

- `input_execute`
- `input_angles`

## Outputs

- `output`

# Operator `math_remap_float`

## Inputs

- `input_execute`
- `input`
- `input_min`
- `input_max`
- `input_map_min`
- `input_map_max`

## Outputs

- `output`

# Operator `math_curve_2d_4knot`

## Inputs

- `input_execute`
- `input`
- `input_X1`
- `input_Y1`
- `input_X2`
- `input_Y2`
- `input_X3`
- `input_Y3`
- `input_X4`
- `input_Y4`

## Outputs

- `output`

# Operator `math_random`

## Inputs

- `input_execute`
- `input_min`
- `input_max`
- `input_seed`

## Outputs

- `output`

# Operator `math_logic_switch`

## Inputs

- `input_execute`
- `input1`
- `input2`
- `input_switch`

## Outputs

- `output`

# Operator `get_soundmixer`

## Inputs

- `input_execute`

## Outputs

- `output_volume`
- `output_level`
- `output_dsp`

# Operator `sys_mixlayer`

## Inputs

- `input_execute`
- `input`

# Operator `calc_occlusion`

## Inputs

- `input_execute`
- `input_trace_interval`
- `input_scalar`
- `input_position`

## Outputs

- `output`

# Operator `set_opvar_float`

## Inputs

- `input_execute`
- `input`

# Operator `get_opvar_float`

## Inputs

- `input_execute`

## Outputs

- `output`
- `output_opvar_exists`

# Operator `increment_opvar_float`

## Inputs

- `input_execute`
- `input`

## Outputs

- `output`
- `output_opvar_exists`

# Operator `sys_output`

## Inputs

- `input_execute`
- `input_speakers`
- `input_vec3`
- `input_float`

# Operator `sys_platform`

## Inputs

- `input_execute`

## Outputs

- `output`

# Operator `game_view_info`

## Inputs

- `input_execute`
- `input_source_index`

## Outputs

- `output_position`
- `output_position_x`
- `output_position_y`
- `output_position_z`
- `output_angles`
- `output_velocity_vector`
- `output_velocity_vector_x`
- `output_velocity_vector_y`
- `output_velocity_vector_z`
- `output_velocity`
- `output_velocity_xy`

# Operator `util_pos_vec8`

## Inputs

- `input_execute`
- `input_index`
- `input_entry_count`
- `input_position_0`
- `input_position_1`
- `input_position_2`
- `input_position_3`
- `input_position_4`
- `input_position_5`
- `input_position_6`
- `input_position_7`

## Outputs

- `output_position`
- `output_max_index`

# Operator `get_source_info`

## Inputs

- `input_execute`
- `input_source_index`

## Outputs

- `output_entity_index`
- `output_position`
- `output_angles`
- `output_radius`
- `output_volume`
- `output_level`
- `output_pitch`
- `output_source_count`

# Operator `calc_spatialize_speakers`

## Inputs

- `input_execute`
- `input_radius`
- `input_radius_max`
- `input_radius_min`
- `input_time_start_stereo_spread`
- `input_time_finish_stereo_spread`
- `input_final_stereo_spread`
- `input_rear_stereo_scale`
- `input_distance`
- `input_position`

## Outputs

- `output`

# Operator `sys_start_entry`

## Inputs

- `input_execute`
- `input_start`
- `input_start_delay`

# Operator `sys_stop_entries`

## Inputs

- `input_execute`
- `input_max_entries`
- `input_stop_delay`

## Outputs

- `output_entries_matching`
- `output_this_matches_index`

# Operator `get_sys_time`

## Inputs

- `input_execute`

## Outputs

- `output_client_time`
- `output_host_time`

# Operator `get_track_syncpoint`

## Inputs

- `input_execute`
- `input_min_time_to_next_sync`
- `input_max_time_to_next_sync`

## Outputs

- `output_first_syncpoint`
- `output_last_syncpoint`
- `output_time_to_next_syncpoint`

# Operator `track_queue`

## Inputs

- `input_execute`

## Outputs

- `output_time_to_next_syncpoint`
- `output_time_to_start`

# Operator `track_update`

## Inputs

- `input_execute`

# Operator `track_stop`

## Inputs

- `input_execute`

# Operator `util_print_float`

## Inputs

- `input_execute`
- `input`

## 📚 Variable Dictionary

For sensors.csv

| **Variable**         | **Unit / Type**      | **Description** |
|----------------------|----------------------|-----------------|
| `timestamp`          | `int64 (ns)`         | Unix timestamp in nanoseconds (10 Hz) |
| `date_GPS`             | `string / datetime`  | Human-readable timestamp of the GPS (corrected offset of 2.1 s). |
| `cts_GPS`              | `ms (float)`              | Elapsed time of the GPS |
| `GPS (Lat.)`         | `° (float)`          | Latitude coordinate. |
| `GPS (Long.)`        | `° (float)`          | Longitude coordinate. |
| `GPS (Alt.)`         | `m (float)`          | Altitude above mean sea level. |
| `GPS (2D speed)`     | `m/s (float)`        | Horizontal ground speed from GPS. |
| `precision`          | `int`                | Precision of the GPS (i.e. number of satellites) |
| `date_gyro`             | `string / datetime`  | Human-readable timestamp of the Gyroscope |
| `cts_gyro`              | `ms (float)`              | Elapsed time of the gyroscope|
| `Gyroscope (x)`      | `rad/s (float)`      | Angular velocity around **X** (roll). |
| `Gyroscope (y)`      | `rad/s (float)`      | Angular velocity around **Y** (pitch). |
| `Gyroscope (z)`      | `rad/s (float)`      | Angular velocity around **Z** (yaw). |
| `date_acc`             | `string / datetime`  | Human-readable timestamp of the  accelerometer |
| `cts_acc`              | `ms (float)`              | Elapsed time of the accelerometer|
| `Accelerometer (x)`   | `m/s^2`         | Acceleration accross X axis. |
| `Accelerometer (y)`   | `m/s^2`         |Acceleration accross X axis. |
| `Accelerometer (z)`   | `m/s^2`          | Acceleration accross X axis. |
| `Accelerometer (x) Filtered`   | `m/s^2`         | Low-pass filtered acceleration (fc= 1 Hz) accross X axis. |
| `Accelerometer (y) Filtered`   | `m/s^2`         | Low-pass filtered acceleration (fc= 1 Hz) accross Y axis. |
| `Accelerometer (z) Filtered`   | `m/s^2`          | Low-pass filtered acceleration (fc= 1 Hz) accross Z axis. |
| `Filtered veloicty [m/s]`   | `m/s`          | Low-pass filtered speed from the GPS (fc= 10 Hz). |
| `Bearing`   | `° (float)`          | Instantaneous heading computed from successive GPS positions. 0° corresponds to North, 90° to East, 180° to South, and 270° to West |
| `frame_index`.  | `int`           | Index of the video frame. Linked with Other_road_users.csv            |


For Other_road_users.csv

| **Variable**     | **Unit / Type** | **Description**                                        |
| ------------- | --------------- | ------------------------------------------------------ |
| `frame_index`.  | `int`           | Index of the video frame. Linked with sensors.csv            |
| `track_id`      | `int`           | Unique ID for each detected pedestrian (tracking).     |
| `class_name`    | `string`        | Class label detected by YOLO     |
| `angle`         | `° (float)`     | Angle of pedestrian relative to vehicle (0 = forward). |
| `distance`      | `m (float)`     | Estimated distance from vehicle.                       |
| `x`             | `m (float)`        | Raw X coordinate relative to the rider (0,0)      |
| `y`             | `m (float)`          | Raw Y coordinate elative to the rider (0,0)    |
| `x_inter`     | `m (float)`        | Interpolated (linearly) X coordinates. |
| `y_inter`     |`m (float)`          | Interpolated (linearly)  Y coordinates.                             |
| `x_inter_rts` | `m (float)`        | Post_processed X  (RTS smoother)     |
| `y_inter_rts` | `m (float)`         | Post_processed Y  (RTS smoother)                           |
| `vx_rts`      | `m/s (float)`   | Smoothed velocity in X (RTS).                          |
| `vy_rts`      | `m/s (float)`   | Smoothed velocity in Y (RTS).                          |
| `interpolated`  | `Bool`   | Dummy indicating if the (x,y) was reconstructed (i.e. interpolated)                     |
| `corrected_class`  | `string`   | Corrected class label (manually or max occurences)                  |


## 📝 Notes

- 
- The data from the sensors were sycnronized based on the nearest timestamps with a tolerance of 0.2 ms.

- The two datasets are in different frequency (i.e. 10 Hz and 24 Hz) and are linked by the column  `frame_index`. 

- The sanity of the dataset could not be checked in one week. Please report any mistakes or weird things you may find. 

## Questionnaires

- Several questionnaires have been used with the NASA-TLX, CBQ, Experience level and demographic. The template of each questionnaire are available in the common folder but we did not include demographics in the dataset as being homogeneous, few and sensitive.

- The NASA Task Load Index (NASA-TLX) measures perceived workload across six dimensions: mental demand, physical demand, temporal demand, performance, effort, and frustration, and has been filled by the riders after their ride of each scenario. 

- The Cycling Behavior Questionnaire (CBQ) assesses various aspects of cycling behavior, including violations, errors, and positive cycling behaviors. Items 1 to 8 refer to violations, items 9 to 23 to errors, and items 24 to 29 to positive behaviors.

- Experience level related questions focus on the stated riding experience level of a ridder with a given MMV.

- For scenario 2, MMV starting by meeting pedestrians were : Subject_A with ebike, Subject_B with both vehicles, Subject E with e-scooter, Subject H with e-bike and Subject K with e-scooter.

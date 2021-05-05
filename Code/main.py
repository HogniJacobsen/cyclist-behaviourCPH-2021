import cyclist
import pandas as pd

g6 = cyclist.Camera(24032021, "2403_g6_sync", "g6")
g6.read_pkl("2403_g6_sync_yolov5x6_corrected")
g6.unique_id(max_age=90, min_hits=1, iou_threshold=0.10, save_load = "load")
g6.cyclist_contact_coordiantes()
g6.frame = "/Users/hogni/Documents/GitHub/cyclist-behaviourCPH-2021/Code/assets/corrected_g6.jpg"
g6.smooth_tracks(20)
src = g6.click_coordinates(g6.frame, dst = "src", type = "load")
dst = g6.click_coordinates(g6.map_path, dst = "dst", type = "load")
g6.find_homography_matrix(src, dst)
g6.transform_points()

s7 = cyclist.Camera(24032021, "2403_s7_sync", "s7")
s7.read_pkl("2403_s7_sync_yolov5x6_corrected")
s7.unique_id(max_age=90, min_hits=1, iou_threshold=0.10, save_load = "load")
s7.cyclist_contact_coordiantes()
s7.frame = "/Users/hogni/Documents/GitHub/cyclist-behaviourCPH-2021/Code/assets/corrected_s7.jpg"
s7.smooth_tracks(20)
src = s7.click_coordinates(s7.frame, dst = "src", type = "load")
dst = s7.click_coordinates(s7.map_path, dst = "dst", type = "load")
s7.find_homography_matrix(src, dst)
s7.transform_points()

remove_line = g6.click_coordinates(g6.map_path, dst = 0, type = "line")
g6.remove_point_line(remove_line, "below")
s7.remove_point_line(remove_line, "above")

def join_df(df_list):
    return pd.concat(df_list, ignore_index=True).sort_values("frame_id").reset_index(drop=True)

joined_df = join_df([g6.tracker_df, s7.tracker_df])
joined = cyclist.Camera(24032021, "joined", "joined")
joined.tracker_df = joined_df
joined.new_bbox(10)
joined.df_format()
joined.unique_id(max_age=90, min_hits=1, iou_threshold=0.10, save_load = "new")

joined.tracker_df.to_csv("/Users/hogni/Documents/GitHub/cyclist-behaviourCPH-2021/Code/Data/24032021/Data/CSV/joined_df_corrected_90_1_0.10_bbox10.csv")

joined.smooth_tracks(20)
joined.tracker_df.to_csv("/Users/hogni/Documents/GitHub/cyclist-behaviourCPH-2021/Code/Data/24032021/Data/CSV/joined_df_corrected_90_1_0.10_bbox10_smooth.csv")

if __name__ == "__main__":
    pass

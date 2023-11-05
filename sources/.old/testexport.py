x_range = (23.75, 24.10)
y_range = (54.81, 54.96)

def filter_data(row):
    if row['geometry_y'] is not None and \
       x_range[0] <= row['geometry_y'].centroid.x <= x_range[1] and \
       y_range[0] <= row['geometry_y'].centroid.y <= y_range[1]:
        return True
    return False


# mask = (geo_data_merged['geometry_y'].notna()) & \
#        (geo_data_merged['geometry_y'].within(geo_data_merged.geometry_y.envelope)) & \
#        (geo_data_merged['eco_normalised'].notna()) & \
#        (geo_data_merged['pop_normalised'].notna()) & \
#        (geo_data_merged['color'].notna())
       # (geo_data_merged['geometry_y'].apply(lambda poly: poly.bounds[0] >= x_range[0] and poly.bounds[2] <= x_range[1] and poly.bounds[1] >= y_range[0] and poly.bounds[3] <= y_range[1]))

# filtered_data = geo_data_merged[mask]

# filtered_df = filtered_data[filtered_data.apply(filter_data, axis=1)]

filtered_df = geo_data_merged[
    (geo_data_merged['geometry_y'].notna()) &
    (geo_data_merged['normalised'].notna()) &
    (geo_data_merged['color'].notna()) &
    (geo_data_merged['pop_normalised'].notna()) &
    (geo_data_merged['eco_normalised'].notna()) &
    (geo_data_merged['geometry_y'].apply(lambda poly: poly.bounds[0] >= x_range[0] and poly.bounds[2] <= x_range[1] and poly.bounds[1] >= y_range[0] and poly.bounds[3] <= y_range[1]))
]


filtered_df.to_csv('filtered_data.csv', index=False)

selected_columns = ['geometry_y', 'normalised', 'color', 'pop_normalised', 'eco_normalised']

#filtered_df[selected_columns].to_csv('kaunasGeographicData.csv', index=False)
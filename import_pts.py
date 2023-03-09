import json



def import_json(json_path):
    json_file = open(json_path)
    json_data = json.load(json_file)
    src_points = [[0 for j in range(5)] for i in range(len(json_data['points']))]
    
    for i in range(len(json_data['points'])):
        src_points[i][0] = json_data['points'][i]['dsc_id']
        x1 = json_data['points'][i]['pts_3d']['X1']
        y1 = json_data['points'][i]['pts_3d']['Y1']
        x2 = json_data['points'][i]['pts_3d']['X2']
        y2 = json_data['points'][i]['pts_3d']['Y2']
        x3 = json_data['points'][i]['pts_3d']['X3']
        y3 = json_data['points'][i]['pts_3d']['Y3']
        x4 = json_data['points'][i]['pts_3d']['X4']
        y4 = json_data['points'][i]['pts_3d']['Y4']
        src_points[i][1] = (x1, y1)
        src_points[i][2] = (x2, y2)
        src_points[i][3] = (x3, y3)
        src_points[i][4] = (x4, y4)
        wx1 = json_data['world_coords']['X1']
        wx2 = json_data['world_coords']['X2']
        wx3 = json_data['world_coords']['X3']
        wx4 = json_data['world_coords']['X4']
        wy1 = json_data['world_coords']['Y1']
        wy2 = json_data['world_coords']['Y2']
        wy3 = json_data['world_coords']['Y3']
        wy4 = json_data['world_coords']['Y4']
        
        
    return src_points
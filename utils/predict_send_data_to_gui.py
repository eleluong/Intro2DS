from mongodb_database import get_last_24h, get_last_7d
import pandas as pd
import yaml
# import torch
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from core.models.lstm import VanillaLSTM

with open('core/config/lstm.yml', encoding='utf-8') as f:
        config = yaml.safe_load(f)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def predict_1_hour(last_24h_df, city):
    config['output_len'] = 1
    model = VanillaLSTM(config, device)
    model = model.load_state_dict(torch.load(f'core/log/lstm/VietNam/change_prediction_length/1/{city}_best.pth')["model_dict"])
    model.eval()
    list_input_ft = config['input_features'][config['dataset']]
    scaler = MinMaxScaler()

    df = last_24h_df[list_input_ft]
    arr = df.iloc[:,:].astype(np.float32).values

    scaler.fit(arr)
    transformed_data = scaler.transform(arr)
    return model(transformed_data)
def predict_6_hour(last_24h_df, city):
    config['output_len'] = 6
    model = VanillaLSTM(config, device)
    model = model.load_state_dict(torch.load(f'core/log/lstm/VietNam/change_prediction_length/2/{city}_best.pth')["model_dict"])
    model.eval()
    list_input_ft = config['input_features'][config['dataset']]
    scaler = MinMaxScaler()

    df = last_24h_df[list_input_ft]
    arr = df.iloc[:,:].astype(np.float32).values

    scaler.fit(arr)
    transformed_data = scaler.transform(arr)
    return model(transformed_data)
def predict_12_hour(last_24h_df, city):
    config['output_len'] = 12
    model = VanillaLSTM(config, device)
    model = model.load_state_dict(torch.load(f'core/log/lstm/VietNam/change_prediction_length/3/{city}_best.pth')["model_dict"])
    model.eval()
    list_input_ft = config['input_features'][config['dataset']]
    scaler = MinMaxScaler()

    df = last_24h_df[list_input_ft]
    arr = df.iloc[:,:].astype(np.float32).values

    scaler.fit(arr)
    transformed_data = scaler.transform(arr)
    return model(transformed_data)
def predict_24_hour(last_24h_df, city):
    config['output_len'] = 24
    model = VanillaLSTM(config, device)
    model = model.load_state_dict(torch.load(f'core/log/lstm/VietNam/change_prediction_length/4/{city}_best.pth')["model_dict"])
    model.eval()
    list_input_ft = config['input_features'][config['dataset']]
    scaler = MinMaxScaler()

    df = last_24h_df[list_input_ft]
    arr = df.iloc[:,:].astype(np.float32).values

    scaler.fit(arr)
    transformed_data = scaler.transform(arr)
    return model(transformed_data)
def send_data_to_gui():
    data = {}
    for city in ['DaNang', 'HaNoi', 'HoChiMinh', 'HungYen', 'NinhBinh']:
        data[city] = {}
        #get 24h from mongodb
        last_24h = get_last_24h(city)
        last_24h_df = pd.DataFrame.from_dict(last_24h)
        data[city]['last_24h'] = last_24h_df
        #current infomation
        current_information = last_24h_df[-1,-6:]
        data[city]['current_infomation'] = current_information
        #historical data (7 days)
        last_7d = get_last_7d(city)
        last_7d_df = pd.DataFrame.from_dict(last_7d)
        data[city]['last_7d_df'] = last_7d_df
        #prediction next 1h
        prediction_next_1h = predict_1_hour(last_24h_df, city)
        data[city]['prediction_next_1h'] = prediction_next_1h
        #prediction next 6h
        prediction_next_6h = predict_6_hour(last_24h_df, city)
        data[city]['prediction_next_6h'] = prediction_next_6h
        #prediction next 12h
        prediction_next_12h = predict_12_hour(last_24h_df, city)
        data[city]['prediction_next_12h'] = prediction_next_12h
        #prediction next 24h
        prediction_next_24h = predict_24_hour(last_24h_df, city)
        data[city]['prediction_next_24h'] = prediction_next_24h
    return data

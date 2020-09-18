import dash
import dash_table
import pandas as pd
import re
import dash_core_components as dcc
import dash_html_components as html


df = pd.read_excel('Bosch_UK_BEL523MS0B_AllInfo_Example.xlsx',
                   sheet_name=1,index_col =0)
                   
#设置列名格式为 “品牌-国家-型号”
cols = []
for i in range(df.shape[1]):
    cols.append(df.loc['Brand'][i] + ' ' + df.loc['Country'][i] + ' ' +df.loc['Mode'][i])
    
df.columns = cols

for i in range(df.shape[1]):
    if re.search(r'(.+),',df.loc['Image Url'][i]):
        df.loc['Image Url'][i] = '![mwo](' + re.findall(r'(.+),',df.loc['Image Url'][i])[0] + ')'
    else:
        None

df = df.reset_index()


app = dash.Dash(__name__)
server = app.server

#初始值
mod = 'Siemens UK S1'

def commodity_table(brand,country,model):
    global mod
    if brand=='All Brands of Region' or country =='All Regions of Brands':
            None
    else:
        mod = brand + ' ' + country + ' '+ model
    table =  dash_table.DataTable(
    id='table',
    columns=[
        {"name": 'ProItem', "id": 'ProItem','presentation':'markdown'},
        {"name": 'Model 1', "id": mod, 'presentation': 'markdown'}, #, 'presentation': 'markdown'
        {"name": 'Model 2', "id": 'Siemens UK S1', 'presentation': 'markdown'},
        #{"name": 'Model 2', "id": 'Model2', 'presentation': 'markdown'},       
    ],
    style_data_conditional=[
        {
            'if': {
                'row_index': 0,
            },
            #'backgroundColor': 'grey',
            'presentation': 'markdown',
            'color': 'dark'
        },
    ],  
    css=[
           dict(selector='img[alt=mwo]', rule='height: 100px;') ,
         {'selector': 'table', 'rule': 'table-layout: fixed'}
        ],

    data=df.to_dict('records'))
        
    return table




#根据图表读取B,C,M，后续根据图表结构修改
dft = df.iloc[:2,1:]
dft = dft.append(df.iloc[3,1:])
dft = dft.T
dft.columns = ['Brand','Country','Model']

counts = ['All Regions of Brands']
[counts.append(i) for i in dft['Country'].unique().tolist()]
brands = ['All Brands of Region']
[brands.append(i) for i in dft['Brand'].unique().tolist()]
    
app.layout = html.Div(
        children = [
            #品牌下拉框
                html.Div([
                    dcc.Dropdown(
                    id='brand-dropdown',
                    options=[{'label': k, 'value': k} for k in brands],
                value='All Brands of Region',
                ),
                html.Div(id='dd-output-container')
                ],
                className = 'drop-down'),
                html.Br(),  
            
                #国家下拉框
                html.Div([
                    dcc.Dropdown(
                    id='country-dropdown',
                    options = [{'label':i,'value':i} for i in counts],
                    value = 'All Regions of Brands'
                ),
                html.Div(id='dd-output-container-brand')
                ],
                className = 'drop-down'),
                html.Br(),
            
                #型号下拉框
                html.Div([
                    dcc.Dropdown(
                    id='model-dropdown',
                #disabled = False,
                value='S1'
                ),
                html.Div(id='dd-output-container-model')
                ]),
                html.Br(),
            ]
        )

#根据品牌更新国家dropdown
@app.callback(
    dash.dependencies.Output('country-dropdown', 'options'),
    [dash.dependencies.Input('brand-dropdown', 'value')])
def set_country_options(selected_brand):
    if selected_brand == 'All Brands of Region':
        country_list = [{'label': i, 'value': i} for i in counts]
    else:
        country_list = [{'label': i, 'value': i} for i in dft[dft['Brand']==selected_brand]['Country'].unique().tolist()]
        country_list.insert(0,{'label':'All Regions of Brands' , 'value': 'All Regions of Brands'})
        
    return country_list



#根据国家更新品牌dropdown
@app.callback(
    dash.dependencies.Output('brand-dropdown', 'options'),
    [dash.dependencies.Input('country-dropdown', 'value')])
def set_country_options(selected_country):
    if selected_country == 'All Regions of Brands':
        brand_list = [{'label': i, 'value': i} for i in brands]
    else:
        brand_list = [{'label': i, 'value': i} for i in dft[dft['Country']==selected_country]['Brand'].unique().tolist()]
        brand_list.insert(0,{'label': 'All Brands of Region', 'value': 'All Brands of Region'})
    return brand_list

#设置型号option
@app.callback(
    dash.dependencies.Output('model-dropdown', 'options'),
    [dash.dependencies.Input('brand-dropdown', 'value'),
    dash.dependencies.Input('country-dropdown', 'value')])
def set_model_option(brand,country):
    option_list = [{'label': i, 'value': i} for i in dft[(dft['Brand']==brand) & (dft['Country']==country)]['Model'].tolist()]
    return option_list

#根据B,C,M返回text , table
@app.callback(
    dash.dependencies.Output('dd-output-container-model', 'children'),
    [dash.dependencies.Input('brand-dropdown', 'value'),
     dash.dependencies.Input('country-dropdown', 'value'),
    dash.dependencies.Input('model-dropdown', 'value')])

def update_output(brand,country,model):
    return 'Brand:{}, Country:{}, Model:{}'.format(brand,country,model),commodity_table(brand,country,model)


if __name__ == '__main__':
    app.run_server(debug=True)
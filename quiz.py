import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Create the Dash application
app = dash.Dash(__name__)

# Define the question and answer
question = {
    "question": "Jupyter Notebook supports which programming language kernels?",
    "options": ["Python", "R", "Julia", "All of the above"],
    "answer": "All of the above"
}

# Application layout
app.layout = html.Div([
    html.H1("Quiz"),
    html.Div([
        html.Div(question["question"]),
        dcc.RadioItems(
            id='question-radio',
            options=[{'label': opt, 'value': opt} for opt in question["options"]],
            value=None
        ),
        html.Button('Submit', id='submit-button', n_clicks=0),
        html.Div(id='output-container')
    ])
])

# Callback to handle answer submission
@app.callback(
    Output('output-container', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('question-radio', 'value')]
)
def update_output(n_clicks, selected_option):
    if n_clicks > 0:
        if selected_option == question["answer"]:
            return "Correct!"
        else:
            return f"Incorrect, the correct answer is: {question['answer']}"

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
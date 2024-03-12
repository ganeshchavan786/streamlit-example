import streamlit as st
from flasgger import Swagger

# Create a Streamlit app
st.title("My Streamlit App with Swagger")

# Initialize Swagger UI
swagger = Swagger()

# Define a route for Swagger UI
@st.cache
def load_swagger():
    swagger_doc = {
        'info': {
            'title': 'My Streamlit API',
            'description': 'An example of how to create a Streamlit API with Swagger',
            'version': '1.0'
        },
        'host': 'localhost:8501',  # Update with your host
        'basePath': '/',
        'schemes': ['http', 'https'],
    }
    return swagger_doc

# Display Swagger UI
load_swagger()

# Your API endpoints
@st.cache
def my_endpoint(param):
    """
    Endpoint description here
    ---
    parameters:
      - name: param
        in: query
        type: string
        required: true
        description: Parameter description
    responses:
      200:
        description: Successful operation
    """
    # Your API logic here
    return "Response"

# Get user input
user_input = st.text_input("Enter parameter:")

# Call your API endpoint
if st.button("Submit"):
    result = my_endpoint(user_input)
    st.write("Result:", result)

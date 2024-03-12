import streamlit as st

# Define a function to handle API requests
def my_api_function(input_data):
    # Process input data and return some output
    output_data = input_data * 2
    return output_data

# Streamlit app code
def main():
    st.title('My Streamlit API')

    # Add input field for users to enter data
    input_data = st.number_input('Enter a number')

    # Add a button to trigger the API request
    if st.button('Run API'):
        # Call the API function with the input data
        output = my_api_function(input_data)
        st.write('Output:', output)

# Run the app
if __name__ == '__main__':
    main()

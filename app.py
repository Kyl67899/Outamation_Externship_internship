!pip install --upgrade gradio gradio

print("Dependancies has been updated")

import gradio as gr
import math

# Create a function to caluclate the sq, cu, and factorial
def calculate_math_value(num):
  # Ensure the input is treated as an integer for factorial
  num = int(num)
  sq = num ** 2
  cu = num ** 3
  even = num % 2 == 0 if num % 2 == 0 else "False"
  fa = math.factorial(num) if num >= 0 else "N/A (Negative)"
  return  sq, cu, even, fa

# using library Gradio to create a web UI interface
demo = gr.Interface(
    fn = calculate_math_value,
    inputs = gr.Number(label="Enter a number"),
    outputs=[
        gr.Number(
            label="Square"
        ),
        gr.Number(
            label="Cube"
        ),
        gr.Number(
            label="Even or odd"
        ),
        gr.Number(
            label="Factorial"
        )
    ],
    title="Math Calculator",
    description="Enter a number to see its square, cube, even, odd and factorial."
)

demo.launch(share=True, debug=True)

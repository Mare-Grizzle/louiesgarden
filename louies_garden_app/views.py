from django.shortcuts import render
from .custom_forms import AddForm
from .custom_forms import AddAskForm
from .gpt3_api import GPT3
from .dalle_api import DALLE
from .constants import VEGETABLE_CHOICES


def planner(request):
    gpt3 = GPT3()
    dalle = DALLE()
    generated_text = ""
    generated_text_list = []
    image_url = ""
    rows = []
    
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            zipcode = form.cleaned_data['zipcode']
            vegetables = form.cleaned_data.get('vegetables', [])
            
            prompt = f"""
                I am an AI that provides information about planting. 
                I am asked to generate a planting layout for a garden. 
                The rows should be numbered and each row should have specific plant recommendations 
                including the number of starter plants or seeds, spacing, and other relevant details. 
                This should depend on the ideal planting date. If today's date is later than the latest plant day for seeds,
                the suggestion should be starters.
                Suggest what to interplant with each vegeatable to avoid common pests. 
                Append each new row with /n,

                For example:
                ,Row 1:, Tomatoes, 3 rows 17 feet each - 30 inches between rows - 6 starter plants - 12 inches apart, Interplant with basil, Plant starters by March 20th, Harvest by Aug 31st /n,
                ...
                Row 9:, Green beans, 2 rows 17 feet each - 18 inches between rows - 102 seeds - 4 inches apart, Interplant with suggested, Plant starters by March 20th, Harvest by Aug 31st /n,
                ...

                The garden dimensions are {height}ft x {width}ft and the user wants to plant {vegetables}. 
                Since the user lives in {zipcode}, include the earliest date the vegetable should be planted due to the average frost. 
                Also include the expected harvest date.
                Please provide a layout for the user's garden, considering their preferences and the garden's dimensions.
            """

            generated_text = gpt3.generate_text(prompt)
            generated_text_list = generated_text.split('/n') if generated_text else []
            rows = [row.split(',') for row in generated_text_list]
            #image_prompt = "garden"
            #image_urls = dalle.generate_image(image_prompt)
            #image_url = image_urls[0] if image_urls else ""
    else:
        form = AddForm()

    return render(request, 'louies_garden_app/planner.html', {
        'form': form,
        'width': width if 'width' in locals() else '',
        'height': height if 'height' in locals() else '',
        'zipcode': zipcode if 'zipcode' in locals() else '',
        'vegetables': vegetables if 'vegetables' in locals() else [],
        'generated_text_list': generated_text_list,
        'rows': rows,
    })

def ask(request):
    gpt3 = GPT3()
    generated_text = ""
    
    if request.method == 'POST':
        form = AddAskForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            
            prompt = f"""
                I am an AI that provides information about gardening, planting, vegetables, fruits, pest control. 
                I am asked to respond a user's question about gardening.
                The user's question is {question}
                Answer the question in a nice, and friendly tone.
                End with "God bless" or "Have a nice day"
            """

            generated_text = gpt3.generate_text(prompt)
    else:
        form = AddAskForm()

    return render(request, 'louies_garden_app/ask.html', {
        'form': form,
        'question': question if 'question' in locals() else '',
        'generated_text': generated_text,
    })

    

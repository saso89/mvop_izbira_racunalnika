import numpy as np

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.serializers.json import DjangoJSONEncoder
from django.template import loader
from django.http import HttpResponse

from .service.dex import DEXModel

from django.conf import settings

from .forms import DexForm, DexFormWithDescription

import logging

logger = logging.getLogger("nakup_televizorja")


class NumpyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(self, obj)


def index(request):
    dex = DEXModel(settings.DEX_MODEL)
    template = loader.get_template('nakup_televizorja/index.html')
    context = {'form': DexFormWithDescription(dex.get_input_attributes_with_descriptions())}
    return HttpResponse(template.render(context, request))


@require_http_methods(["POST"])
def results(request):
    dex = DEXModel(settings.DEX_MODEL)
    form = DexForm(dex.get_input_attributes(), request.POST)
    if form.is_valid():
        quantitative_response, qualitative_response = dex.evaluate_model(form.cleaned_data)
        template = loader.get_template('nakup_televizorja/results.html')
        context = {'quantitative_response': quantitative_response}
        return HttpResponse(template.render(context, request))
    return render(request, "index.html", {"form": form})

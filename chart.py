# -*- coding: utf-8 -*-

# Author: Rodrigo E. Principe
# Email: fitoprincipe82 at gmail

import pygal
import math


class Chart(pygal.XY):
    def __init__(self, **kwargs):
        super(Chart, self).__init__(**kwargs)

    def fill_chart(self, dataset):
        """ fill data of the chart with a dataset containing:
            [[[x1, y1], category1], [[x2, y2], category2],.., [[xn, yn], categoryn]]
        """
        # get categories
        categories = {}
        for row in dataset:
            category = row[1]
            categories[category] = []

        for row in dataset:
            data = row[0]
            category = row[1]
            categories[category].append(data)

        for cat, vector in categories.items():
            self.add(str(cat), vector)

    def add_trend_line(self, bias, weights, name='trend line'):
        xvalues = self.get_xvals()
        values = []
        for x in xvalues:
            y = (-weights[0]*x - bias)/weights[1]
            values.append([x, y])
        self.add(name, values, stroke=True)

    def get_xvals(self):
        raw = self.raw_series
        min_xs = []
        max_xs = []
        for serie in raw:
            values = serie[0]
            title = serie[1]['title']
            xs = [e[0] for e in values]
            min_xs.append(min(xs))
            max_xs.append(max(xs))
        min_value = math.floor(min(min_xs))
        max_value = math.floor(max(max_xs))
        return list(range(min_value, max_value+1))

    def render_widget(self, width=None, height=None):
        """ Render a pygal chart into a Jupyter Notebook """
        from ipywidgets import HTML
        import base64

        b64 = base64.b64encode(chart.render()).decode('utf-8')

        src = 'data:image/svg+xml;charset=utf-8;base64,'+b64

        if width and not height:
            html = '<embed src={} width={}></embed>'.format(src, width)
        elif height and not width:
            html = '<embed src={} height={}></embed>'.format(src, height)
        elif width and height:
            html = '<embed src={} height={} width={}></embed>'.format(src,
                                                                      height,
                                                                      width)
        else:
            html = '<embed src={}>'.format(src)

        return HTML(html)


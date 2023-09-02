FROM python:3

#todo: use requirements
RUN pip3 install --upgrade "voila" \
	         "nbconvert" \
		 "ipython[all]" \
		 "pandas" \
		 "plotly" \
		 "scipy"
RUN useradd -ms /bin/bash voila

EXPOSE 8866

USER voila
WORKDIR /home/voila

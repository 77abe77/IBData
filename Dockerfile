FROM python:3.6.2

WORKDIR /spartanio/src
ADD . /spartanio/src

ENV ENVIRONMENT production
ENV PYTHONUSERBASE /venv
ENV PATH "/venv/bin:${PATH}"
ENV PYTHONPATH "$PYTHONPATH:/spartanio/src:/spartanio/src/tests"
ARG GITHUB_TOKEN
RUN ./docker/setup.sh

EXPOSE 5000

ENTRYPOINT ["./docker/entrypoint.sh"]
CMD ["./manage.py", "run_production_server"]

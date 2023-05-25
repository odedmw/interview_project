import unittest
import yaml
from code import *


class YamlEditorTests(unittest.TestCase):
    def test_bigger_then_1_replace_value(self):
        expected_result = """
apiVersion: machinelearning
kind: SeldonDeployment
metadata:
  labels:
    app: seldon
  name: seldon-deployment-{{workflow.name}}
  namespace: kubeflow
spec:
  annotations:
    deployment_version: v1
    project_name: NLP Pipeline
  name: seldon-deployment-{{workflow.name}}
  predictors:
  - annotations:
      predictor_version: v1
    componentSpecs:
    - spec:
        containers:
        - image: tfidf_vectorizer:0.1,
          imagePullPolicy: IfNotPresent,
          name: tfidfvectorizer
        volumes:
        - name: mypvc
          persistentVolumeClaim:
            claimName: '{{workflow.name}}-my-pvc'
    graph:
      children:
      - endpoint:
          type: REST
        name: spacytokenizer
        """
        with open(__file__.replace("\\", "/").replace("test.py", "original_yaml.yml")) as read_obj:
            input_yaml = yaml.safe_load(read_obj)
            with open(__file__.replace("\\", "/").replace("test.py", "test_bigger_then_1.yml")) as additional_conf:
                config_input = yaml.safe_load(additional_conf)
                keep_or_lose = False
                if isinstance(config_input, dict):
                    get_all_key_paths_in_json(input_yaml, input_yaml, config_input, keep_or_lose)
                else:
                    for i in config_input:
                        get_all_key_paths_in_json(input_yaml, input_yaml, i, keep_or_lose)
                input_yaml = yaml.dump(input_yaml)
                expected_result = yaml.safe_load(expected_result)
                expected_result = yaml.dump(expected_result)
                self.assertEqual(expected_result, input_yaml)

    def test_bigger_then_1_keep_value(self):
        expected_result = """
apiVersion: machinelearning
kind: SeldonDeployment
metadata:
  labels:
    app: seldon
  name: seldon-deployment-{{workflow.name}}
  namespace: kubeflow
spec:
  annotations:
    deployment_version: v1
    project_name: NLP Pipeline
  name: seldon-deployment-{{workflow.name}}
  predictors:
  - annotations:
      predictor_version: v1
    componentSpecs:
    - spec:
        containers:
        - image: clean_text_transformer:0.1
          imagePullPolicy: IfNotPresent
          name: cleantext
        - image: tfidf_vectorizer:0.1,
          imagePullPolicy: IfNotPresent,
          name: tfidfvectorizer
        volumes:
        - name: mypvc
          persistentVolumeClaim:
            claimName: '{{workflow.name}}-my-pvc'
    graph:
      children:
      - endpoint:
          type: REST
        name: spacytokenizer
        """
        with open(__file__.replace("\\", "/").replace("test.py", "original_yaml.yml")) as read_obj:
            input_yaml = yaml.safe_load(read_obj)
            with open(__file__.replace("\\", "/").replace("test.py", "test_bigger_then_1.yml")) as additional_conf:
                config_input = yaml.safe_load(additional_conf)
                keep_or_lose = True
                if isinstance(config_input, dict):
                    get_all_key_paths_in_json(input_yaml, input_yaml, config_input, keep_or_lose)
                else:
                    for i in config_input:
                        get_all_key_paths_in_json(input_yaml, input_yaml, i, keep_or_lose)
                input_yaml = yaml.dump(input_yaml)
                expected_result = yaml.safe_load(expected_result)
                expected_result = yaml.dump(expected_result)
                self.assertEqual(expected_result, input_yaml)

    def test_length_1_replace_value(self):
        expected_result = """
apiVersion: example
kind: SeldonDeployment
metadata:
  labels:
    app: seldon
  name: seldon-deployment-{{workflow.name}}
  namespace: kubeflow
spec:
  annotations:
    deployment_version: v1
    project_name: NLP Pipeline
  name: seldon-deployment-{{workflow.name}}
  predictors:
  - annotations:
      predictor_version: v1
    componentSpecs:
    - spec:
        containers:
        - image: clean_text_transformer:0.1
          imagePullPolicy: IfNotPresent
          name: cleantext
        volumes:
        - name: mypvc
          persistentVolumeClaim:
            claimName: '{{workflow.name}}-my-pvc'
    graph:
      children:
      - endpoint:
          type: REST
        name: spacytokenizer
        """
        with open(__file__.replace("\\", "/").replace("test.py", "original_yaml.yml")) as read_obj:
            input_yaml = yaml.safe_load(read_obj)
            with open(__file__.replace("\\", "/").replace("test.py", "test_length_1_example.yml")) as additional_conf:
                config_input = yaml.safe_load(additional_conf)
                keep_or_lose = False
                if isinstance(config_input, dict):
                    get_all_key_paths_in_json(input_yaml, input_yaml, config_input, keep_or_lose)
                else:
                    for i in config_input:
                        get_all_key_paths_in_json(input_yaml, input_yaml, i, keep_or_lose)
                input_yaml = yaml.dump(input_yaml)
                expected_result = yaml.safe_load(expected_result)
                expected_result = yaml.dump(expected_result)
                self.assertEqual(expected_result, input_yaml)

    def test_length_1_keep_value(self):
        expected_result = """
apiVersion:
- machinelearning
- example
kind: SeldonDeployment
metadata:
  labels:
    app: seldon
  name: seldon-deployment-{{workflow.name}}
  namespace: kubeflow
spec:
  annotations:
    deployment_version: v1
    project_name: NLP Pipeline
  name: seldon-deployment-{{workflow.name}}
  predictors:
  - annotations:
      predictor_version: v1
    componentSpecs:
    - spec:
        containers:
        - image: clean_text_transformer:0.1
          imagePullPolicy: IfNotPresent
          name: cleantext
        volumes:
        - name: mypvc
          persistentVolumeClaim:
            claimName: '{{workflow.name}}-my-pvc'
    graph:
      children:
      - endpoint:
          type: REST
        name: spacytokenizer
        """
        with open(__file__.replace("\\", "/").replace("test.py", "original_yaml.yml")) as read_obj:
            input_yaml = yaml.safe_load(read_obj)
            with open(__file__.replace("\\", "/").replace("test.py", "test_length_1_example.yml")) as additional_conf:
                config_input = yaml.safe_load(additional_conf)
                keep_or_lose = True
                if isinstance(config_input, dict):
                    get_all_key_paths_in_json(input_yaml, input_yaml, config_input, keep_or_lose)
                else:
                    for i in config_input:
                        get_all_key_paths_in_json(input_yaml, input_yaml, i, keep_or_lose)
                input_yaml = yaml.dump(input_yaml)
                expected_result = yaml.safe_load(expected_result)
                expected_result = yaml.dump(expected_result)
                self.assertEqual(expected_result, input_yaml)

    def test_nested_length_1_replace_value(self):
        expected_result = """
apiVersion: machinelearning
kind: SeldonDeployment
metadata: example
spec:
  annotations:
    deployment_version: v1
    project_name: NLP Pipeline
  name: seldon-deployment-{{workflow.name}}
  predictors:
  - annotations:
      predictor_version: v1
    componentSpecs:
    - spec:
        containers:
        - image: clean_text_transformer:0.1
          imagePullPolicy: IfNotPresent
          name: cleantext
        volumes:
        - name: mypvc
          persistentVolumeClaim:
            claimName: '{{workflow.name}}-my-pvc'
    graph:
      children:
      - endpoint:
          type: REST
        name: spacytokenizer
        """
        with open(__file__.replace("\\", "/").replace("test.py", "original_yaml.yml")) as read_obj:
            input_yaml = yaml.safe_load(read_obj)
            with open(__file__.replace("\\", "/").replace("test.py", "test_nested_length_1_example.yml")) as additional_conf:
                config_input = yaml.safe_load(additional_conf)
                keep_or_lose = False
                if isinstance(config_input, dict):
                    get_all_key_paths_in_json(input_yaml, input_yaml, config_input, keep_or_lose)
                else:
                    for i in config_input:
                        get_all_key_paths_in_json(input_yaml, input_yaml, i, keep_or_lose)
                input_yaml = yaml.dump(input_yaml)
                expected_result = yaml.safe_load(expected_result)
                expected_result = yaml.dump(expected_result)
                self.assertEqual(expected_result, input_yaml)

    def test_nested_length_1_keep_value(self):
        expected_result = """
apiVersion: machinelearning
kind: SeldonDeployment
metadata: 
- labels:
    app: seldon
  name: seldon-deployment-{{workflow.name}}
  namespace: kubeflow
- example
spec:
  annotations:
    deployment_version: v1
    project_name: NLP Pipeline
  name: seldon-deployment-{{workflow.name}}
  predictors:
  - annotations:
      predictor_version: v1
    componentSpecs:
    - spec:
        containers:
        - image: clean_text_transformer:0.1
          imagePullPolicy: IfNotPresent
          name: cleantext
        volumes:
        - name: mypvc
          persistentVolumeClaim:
            claimName: '{{workflow.name}}-my-pvc'
    graph:
      children:
      - endpoint:
          type: REST
        name: spacytokenizer
        """
        with open(__file__.replace("\\", "/").replace("test.py", "original_yaml.yml")) as read_obj:
            input_yaml = yaml.safe_load(read_obj)
            with open(__file__.replace("\\", "/").replace("test.py", "test_nested_length_1_example.yml")) as additional_conf:
                config_input = yaml.safe_load(additional_conf)
                keep_or_lose = True
                if isinstance(config_input, dict):
                    get_all_key_paths_in_json(input_yaml, input_yaml, config_input, keep_or_lose)
                else:
                    for i in config_input:
                        get_all_key_paths_in_json(input_yaml, input_yaml, i, keep_or_lose)
                input_yaml = yaml.dump(input_yaml)
                expected_result = yaml.safe_load(expected_result)
                expected_result = yaml.dump(expected_result)
                self.assertEqual(expected_result, input_yaml)


if __name__ == '__main__':
    unittest.main()

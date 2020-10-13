from toscaparser.tosca_template import ToscaTemplate
import toscaparser

teste = "/home/sanches/teste.yaml"

teste2 = ToscaTemplate(teste)

# for key in teste2.nodetemplates:
#     print(key.templates)

teste3 = toscaparser.tosca_template.ToscaTemplate
print(teste3)




# teste3 = teste2.nodetemplates
# print(teste3)


# for item in teste3:
#     print(item.templates.get)


# print(teste2.policies)
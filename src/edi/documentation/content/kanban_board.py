# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

statusterms = [SimpleTerm(value="todo", token="todo", title="ToDo"),
               SimpleTerm(value="in_progress", token="in_progress", title="In Progress"),
               SimpleTerm(value="done", token="done", title="Done")]

status = SimpleVocabulary(statusterms)

# from edi.documentation import _

class IKanbanBoard(model.Schema):
    """ Marker interface and Dexterity Python Schema for KanbanBoard
    """


    tasksources = RelationList(
            title = "Ordner mit Tasks auswählen",
            description = "Aus welchen Ordnern sollen die ToDo-Tasks für dieses Kanban-Board angezeigt werden?\
                           Ohne Angabe werden alle ToDo Tasks aus dem Portal angezeigt.",
            required = False,
            default = [],
            value_type = RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
            missing_value=[],
            )

    directives.widget(
            'tasksources',
            RelatedItemsFieldWidget,
            pattern_options={
                'selectableTypes': ['Folder'],
                'basePath': make_relation_root_path,
                },
            )

    workflows = schema.List(
            title = "Workflow-Status auswählen",
            description = "Auswahl welche Workflow-Status im Kanban-Board angezeigt werden sollen?\
                           Ohne Auswahl werden alle Status angezeigt.",
            required = False,
            value_type = schema.Choice(vocabulary=status),
            )


@implementer(IKanbanBoard)
class KanbanBoard(Container):
    """ Content-type class for IKanbanBoard
    """

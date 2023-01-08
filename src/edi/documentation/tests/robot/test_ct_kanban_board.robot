# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.documentation -t test_kanban_board.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.documentation.testing.EDI_DOCUMENTATION_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/documentation/tests/robot/test_kanban_board.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Kanban Board
  Given a logged-in site administrator
    and an add Kanban Board form
   When I type 'My Kanban Board' into the title field
    and I submit the form
   Then a Kanban Board with the title 'My Kanban Board' has been created

Scenario: As a site administrator I can view a Kanban Board
  Given a logged-in site administrator
    and a Kanban Board 'My Kanban Board'
   When I go to the Kanban Board view
   Then I can see the Kanban Board title 'My Kanban Board'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Kanban Board form
  Go To  ${PLONE_URL}/++add++Kanban Board

a Kanban Board 'My Kanban Board'
  Create content  type=Kanban Board  id=my-kanban_board  title=My Kanban Board

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Kanban Board view
  Go To  ${PLONE_URL}/my-kanban_board
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Kanban Board with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Kanban Board title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

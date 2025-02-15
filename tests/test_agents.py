import pytest
from crewai import Agent, Crew, Process, Task
from event_tracker.crew import EventTracker

def test_agent_creation():
    tracker = EventTracker()
    assert hasattr(tracker, 'researcher'), "EventTracker should have a researcher agent"
    assert hasattr(tracker, 'reporting_analyst'), "EventTracker should have a reporting_analyst agent"
    assert isinstance(tracker.researcher(), Agent), "The researcher agent should be an instance of Agent"
    assert isinstance(tracker.reporting_analyst(), Agent), "The reporting_analyst agent should be an instance of Agent"

def test_agent_roles():
    tracker = EventTracker()
    researcher = tracker.researcher()
    reporting_analyst = tracker.reporting_analyst()
    assert researcher.role == "{topic} Senior Data Researcher\n", "The researcher agent should have the correct role"
    assert reporting_analyst.role == "{topic} Reporting Analyst\n", "The reporting analyst agent should have the correct role"

def test_agent_goals():
    tracker = EventTracker()
    researcher = tracker.researcher()
    reporting_analyst = tracker.reporting_analyst()
    assert researcher.goal == "Uncover cutting-edge developments in {topic}\n", "The researcher agent should have the correct goal"
    assert reporting_analyst.goal == "Create detailed reports based on {topic} data analysis and research findings\n", "The reporting analyst agent should have the correct goal"


    
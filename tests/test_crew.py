import pytest
from crewai import Agent, Crew, Process, Task
from event_tracker.crew import EventTracker

def test_crew_creation():
    tracker = EventTracker()
    crew = tracker.crew()
    assert isinstance(crew, Crew), "EventTracker should have a Crew"

def test_crew_attributes():
    tracker = EventTracker()
    crew = tracker.crew()
    assert hasattr(crew, 'agents'), "Crew should have agents"
    assert len(crew.agents) == 2, "Crew should have 2 agents"


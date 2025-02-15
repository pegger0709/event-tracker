import pytest
import os
from pathlib import Path
from crewai import Agent, Crew, Process, Task
from event_tracker.crew import EventTracker

def test_task_creation():
    tracker = EventTracker()
    assert hasattr(tracker, 'research_task'), "EventTracker should have a research task"
    assert hasattr(tracker, 'reporting_task'), "EventTracker should have a reporting task"
    research_task = tracker.research_task()
    reporting_task = tracker.reporting_task()
    assert isinstance(research_task, Task), "Research task should be an instance of Task"
    assert hasattr(research_task, 'config'), "Research task should have a config attribute"
    assert isinstance(reporting_task, Task), "Reporting task should be an instance of Task"
    assert hasattr(reporting_task, 'config'), "Reporting task should have a config attribute"
    assert hasattr(reporting_task, 'output_file'), "Reporting task should have an output file"
    assert reporting_task.output_file == "{output_file}", "Output file should be dynamically defined"


def test_task_execution():
    tracker = EventTracker()
    crew = tracker.crew()  
    temp_file_path = Path("tmp/temp_report.md")
    temp_file_path.touch() # Create the temporary file
    assert temp_file_path.exists(), "tmp file was not created!"
    result = crew.kickoff(
        inputs={"topic": "financial markets", "current_year": "2008", "output_file": str(temp_file_path)}
        #inputs={"topic": "United States politics", "current_year": "2016", "output_file": str(temp_file_path)}
    )  # Execute the task pipeline
    assert hasattr(result, "raw"), "Result should have a raw method"
    result_str = result.raw
    assert isinstance(result_str, str), "Crew should return a result after execution"
    assert "financial crisis" in result_str, "Result should refer to the financial crisis of 2008"
    #assert "Trump" in result_str, "Result should refer to the 2016 election of Donald Trump as President of the United States"
    assert open(temp_file_path, "r").read() == result_str, "Result should be saved to the tmp file"
    temp_file_path.unlink()  # Clean up the temporary file
    assert not temp_file_path.exists(), "tmp file was not deleted!"
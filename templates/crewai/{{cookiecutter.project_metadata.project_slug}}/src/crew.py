from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# TODO: capitalize the first letter of the proj name
@CrewBase
class {{cookiecutter.project_metadata.project_name}}Crew():
	"""{{cookiecutter.project_metadata.project_name}} crew"""

	# Agent definitions
	{%- for agent in cookiecutter.structure.agents %}
	@agent
	def {{agent.name}}(self) -> Agent:
		return Agent(
			config=self.agents_config['{{ agent.name }}'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	{%- endfor %}

	# Task definitions
	{%- for task in cookiecutter.structure.tasks %}
	@task
	def {{task.name}}(self) -> Task:
		return Task(
			config=self.tasks_config['{{task.name}}'],
		)
	{%- endfor %}

	@crew
	def crew(self) -> Crew:
		"""Creates the Test crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
# Research project-management toolkit

A practical set of governance and delivery templates for applied research and evaluation projects. The toolkit connects the analytic plan to scope, roles, risks, decisions, data responsibilities, and acceptance criteria so that project controls support the research rather than becoming separate administrative work.

The example project is fictional. The templates are original and can be adapted to education, public-health, nonprofit, or product-evaluation settings.

## What is included

### Initiation and planning

- project charter
- evaluation plan
- data-management plan
- stakeholder register
- work plan
- requirements traceability matrix

### Monitoring and control

- risk and issue register
- decision log
- status report
- change request
- stage-gate criteria
- definition of done

### GitHub collaboration

- change-request issue form
- risk/issue form
- pull-request template
- automated structural validation for CSV templates

## How the pieces connect

The charter defines why the project exists and what success means. The evaluation plan turns that purpose into questions, measures, methods, and deliverables. The requirements matrix traces each commitment to evidence and acceptance criteria. Risks, decisions, and changes remain visible throughout delivery, while stage gates prevent the team from advancing before prerequisites are met.

## Suggested workflow

1. Approve the charter and decision rights.
2. Complete the stakeholder and requirements registers.
3. Align evaluation questions with measures, sources, methods, and deliverables.
4. Approve data access and the data-management plan.
5. Baseline the work plan.
6. Review risks, issues, decisions, and changes on a regular cadence.
7. Use stage gates before data collection, analysis, interpretation, and release.
8. Close with acceptance, handoff, lessons learned, and an archive inventory.

## Repository structure

~~~text
templates/
  project-charter.md
  evaluation-plan.md
  data-management-plan.md
  work-plan.csv
  stakeholder-register.csv
  risk-register.csv
  decision-log.csv
  requirements-traceability-matrix.csv
  change-request.md
  status-report.md
governance/
  stage-gates.md
  definition-of-done.md
examples/education-evaluation/
  charter.md
  work-plan.csv
  risk-register.csv
.github/ISSUE_TEMPLATE/
scripts/
  validate_templates.py
~~~

## Example scenario

The completed example shows a 16-week evaluation of a fictional literacy-support pilot across twelve sites. It demonstrates realistic sequencing, dependencies, risk ownership, contingency triggers, and deliverable acceptance without using proprietary information.

## Tailoring guidance

Keep only the controls that change a decision or reduce meaningful risk. A short analysis may need a one-page charter and a decision log; a multisite evaluation involving protected data may require all of the templates plus organization-specific privacy, security, and review procedures.

These resources draw on standard project-management and research-governance concepts. They are not a substitute for an organization's policies, IRB requirements, data-use agreements, or legal review.

## Skills demonstrated

Research operations · project planning · scope management · risk management · stakeholder engagement · requirements traceability · change control · evaluation governance · GitHub collaboration

## License

CC BY 4.0

# Scientific argument and section evidence

Use this reference when the task includes derivation, mechanics interpretation, quantitative comparison or figure selection. It is a reusable organization guide, not a prescribed model.

## Section planning

For each section identify:

1. **Purpose.** The physical question and what decision its answer changes.
2. **Sample.** The configuration, boundary conditions, material law, reference coordinates and the variables changed in the comparison.
3. **Inputs.** The particular geometry, raw curves, states, matrices or experiment files used. Distinguish an identified effective model from the physical specimen and identify fitted versus independent comparison data.
4. **Processing.** The equations or postprocessing that turn those inputs into observables. Record units, normalization, sign conventions and numerical tolerances that matter to interpretation.
5. **Observation.** What the curves, shapes or calculations actually show, with representative numbers.
6. **Mechanism.** Which term or constraint explains that observation and what alternative could explain it.
7. **Figure.** The panels needed to connect the sample, result and mechanism. A geometry panel, response panel and a diagnostic panel often work well; do not add all three when one would suffice.
8. **Statement.** The conclusion readers should retain, expressed at the scope supported by the comparison.

Keep useful earlier analyses in the evidence inventory even when they are merged, shortened or moved to SI. Distinguish archival results from calculations valid for the revised geometry. Reusing a stiffness law may be reasonable, but numerical equilibria and instability modes generally require recomputation when connection kinematics change.

## Derivation before interpretation

Start from the actual model. Define the independent nodal coordinates or degrees of freedom, controls, reference geometry and constitutive parameters. Do not copy an illustrative two-coordinate expression over a higher-dimensional model.

For a potential-energy formulation, a useful derivation sequence is:

1. Element and connection kinematics, including any rigid maps or shared nodal degrees of freedom.
2. The complete potential energy and the assumptions behind each contribution.
3. Its first derivatives and the constrained equilibrium equations.
4. The allowed virtual nodal increments under the current boundary and contact state.
5. The second variation on those increments and the physical motion represented by its modes.
6. The connected finite branches or trajectories and the full energy balance between source and endpoint.

Name the model's actual symbols consistently. A generic constrained potential can be written as

\[
\mathcal L(q,\lambda,p;U)=\Pi(q;U)+\lambda^T c(q;U)-p^T g(q;U),
\]

with bilateral constraints \(c=0\), nonpenetration \(g\geq0\), contact multipliers \(p\geq0\), and complementarity \(p_i g_i=0\). Use the sign convention already adopted by the model, and explain any conversion from software reactions to physical quantities.

Here \(d\) is a virtual nodal increment; \(Dg(q)[d]=g_{,q}d\) is the first-order change of gap, rather than an independent displacement. If a matrix \(B\) denotes that contact Jacobian, define its rows, columns and units. Do not reuse \(B\) for the element strain-displacement matrix without distinguishing them.

Use the Hessian of the appropriate Lagrangian, including constraint curvature when present. Eliminate prescribed degrees of freedom and impose connection constraints before evaluating stability. With unilateral contact, distinguish compressed contacts from zero-reaction contacts and check that a tested mode opens rather than penetrates them. Explain any coordinate scaling before comparing eigenvalue magnitudes. Mixed translational and rotational coordinates do not share a numerical unit.

A stable interior equilibrium can lose stability through zero tangent curvature. A contact release can instead admit a previously excluded direction whose released curvature is already negative. A negative curvature direction establishes local energetic instability under the stated assumptions; it does not by itself establish the observed finite landing. At zero curvature, second-order analysis alone is inconclusive.

For finite motion, evaluate the complete energy on a feasible connected route or an appropriately resolved dynamic trajectory. A lower-energy remote equilibrium does not prove that it is the first accessible endpoint. Separate geometric lateral reversal from classical static snap-back in a specified load-control diagram.

## Energy and coupling

Energy bookkeeping by element or constitutive contribution is useful when the full sum is retained. It does not imply independent local energy wells. Do not discard off-diagonal terms or analyze one interaction entry as if it were the entire system.

If condensing internal degrees of freedom, state the equilibrium conditions used to eliminate them, retain their relaxed contribution, and specify when the eliminated block is nonsingular. Interpret a cross derivative as a conditional interaction; actual loading trends also depend on the branch derivatives and imposed control.

A symmetry statement constrains the form or transformation of an operator. It does not determine every coefficient, selected branch or imperfection-sensitive dynamic path. A count, width or orientation trend needs a comparison that actually controls the other relevant variables.

## Figures and concise claims

Use actual sampled points when showing a parameter map; do not invent boundaries between sparse points. Define event criteria independently of attractive-looking oscillations. For analytical-FEM or experimental comparisons, register the same physical observable and distinguish dynamic jumps from equilibrium stability calculations.

A caption should name the sample and control, define its symbols and line/marker meanings, and state the panel's purpose. Put the mechanical interpretation in the prose near the figure. Provide a reference for methods or comparisons that are imported from earlier work.

Prefer a direct statement such as “At this release, the newly permitted opening mode has negative curvature and the upper mouth moves left while the gap increases” over “Eigenvalues prove snapping.” If a comparison is approximate, state which sequence, sign or amplitude agrees and give the relevant discrepancy once.

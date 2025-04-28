+++
title = "Regularized nonlinear parametric approximation of evolution equations"
subtitle = "Course given by Prof. C. Lubich (Tübingen)"
author = "C. Lubich (Tübingen)"
draft = false
LinkTitle = "lubich"
tags = "course"
keywords = ""
begin = "28 April"
end = "30 April"
+++

{{< collapsible_button  
    title="Schedule" 
    text=`
    <table style="margin-left: auto; margin-right: auto;>
  <thead>
    <tr style="text-align: right;">
      <th>Lecture</th>
      <th>Time</th>
      <th>Place</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lecture 1</td>
      <td>09:00-10:45, 28.04.2025</td>
      <td><a href='https://www.google.com/maps/dir//Gran+Sasso+Science+Institute,+Viale+Francesco+Crispi,+7+Rectorate,+Via+Michele+Iacobucci,+2,+67100+L'Aquila+AQ,+Italy/@42.3445687,13.31408'>Main Lecture Hall, Ex-Isef</a></td>
    </tr>
    <tr>
      <td>Lecture 2</td>
      <td>14:15-15:45, 28.04.2025</td>
      <td><a href='https://www.google.com/maps/dir//Gran+Sasso+Science+Institute,+Viale+Francesco+Crispi,+7+Rectorate,+Via+Michele+Iacobucci,+2,+67100+L'Aquila+AQ,+Italy/@42.3445687,13.31408'>Main Lecture Hall, Ex-Isef</a></td>
    </tr>
    <tr>
      <td>Lecture 3</td>
      <td>10:45-12:15, 29.04.2025</td>
      <td><a href='https://www.google.com/maps/dir//Gran+Sasso+Science+Institute,+Viale+Francesco+Crispi,+7+Rectorate,+Via+Michele+Iacobucci,+2,+67100+L'Aquila+AQ,+Italy/@42.3445687,13.31408'>Main Lecture Hall, Ex-Isef</a></td>
    </tr>
    <tr>
      <td>Lecture 4</td>
      <td>09:00-10:45, 30.04.2025</td>
      <td><a href='https://www.google.com/maps/dir//Gran+Sasso+Science+Institute,+Viale+Francesco+Crispi,+7+Rectorate,+Via+Michele+Iacobucci,+2,+67100+L'Aquila+AQ,+Italy/@42.3445687,13.31408'>Main Lecture Hall, Ex-Isef</a></td>
    </tr>
  </tbody>
</table>`
>}}

{{< pbr text="" >}}

This course is about the numerical approximation of evolution equations
by nonlinear parametrizations $u(t)=\Phi(q(t))$ with time-dependent
parameters $q(t)$, which are to be determined in the computation. The
motivation comes from approximations in quantum dynamics by multiple
Gaussians and approximations of various dynamical problems by tensor
networks and neural networks. In all these cases, the parametrization is
typically irregular: the derivative $\Phi'(q)$ can have arbitrarily small
singular values and may have varying rank. We derive approximation results
for a regularized approach in the time-continuous case as well as in
time-discretized cases. With a suitable choice of
the regularization parameter and the time stepsize, the approach can be
successfully applied in irregular situations, even though it runs counter
to the basic principle in numerical analysis to avoid solving ill-posed
subproblems when aiming for a stable algorithm. Numerical experiments with
sums of Gaussians for approximating quantum dynamics and with neural
networks for approximating the flow map of a system of ordinary
differential equations illustrate and complement the theoretical results.
The course is based on joint work with Jörg Nick, Caroline Lasser, and
Michael Feischl:

* [arXiv:2403.19234](https://arxiv.org/abs/2403.19234)
* [arXiv:2501.12118](https://arxiv.org/abs/2501.12118)

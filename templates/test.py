{% extends "layout.html" %}
{% block content %}
input("
<h1>Which report(s) do you want to pullllll? </h1>
<form>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3846202">
      NYS Intro
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3847508">
      Anti-Harassment 1
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3846909">
      Anti-Harassment 5
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3846758">
      Anti-Harassment 6
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3848048">
      Understanding Harassment 1
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3848322">
      Understanding Harassment 2
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3848379">
      Understanding Harassment 3
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3847029">
      Understanding Harassment 4
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3846770">
      Understanding Harassment: 5
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3848626">
      Understanding Harassment 6
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="3848445">
      Understanding Harassment 7
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="4775856">
      NYS Scenarios
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="4673600">
      NYC Intro
    </label>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox" value="4673603">
      NYC Scenarios
    </label>
  </div>
  <div>
      <p>
          Goal: download and format reports based on which checkboxes are selected.
      </p>
  </div>
  <div class="flex">
      <div class = "button">
          <p class="center">Run Report</p>
      </div>
  </div>
</form>
")
{% endblock content %}

/*!

=========================================================
* Argon Design System React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-design-system-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-design-system-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// nodejs library that concatenates classes
import classnames from "classnames";

// reactstrap components
import {
  Badge,
  Button,
  Container,
  Row,
  Col,
  FormGroup,
  Form,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Label,
} from "reactstrap";

// core components
import DemoNavbar from "components/Navbars/DemoNavbar.js";
import SimpleFooter from "components/Footers/SimpleFooter.js";

class Landing extends React.Component {
  state = {};
  componentDidMount() {
    document.documentElement.scrollTop = 0;
    document.scrollingElement.scrollTop = 0;
    this.refs.main.scrollTop = 0;
  }
  render() {
    return (
      <>
        <DemoNavbar />
        <main ref="main">
          <div className="position-relative">
            {/* shape Hero */}
            <section className="section section-lg section-shaped pb-250">
              <div className="shape shape-style-1 shape-default">
                <span />
                <span />
                <span />
                <span />
                <span />
                <span />
                <span />
                <span />
                <span />
              </div>
              <Container className="py-lg-md d-flex">
                <div className="col px-0">
                  <Row>
                    <Col lg="6">
                      <h1 className="display-3 text-white">
                        Crisis Aversion <span>TwitterU Codechella</span>
                      </h1>
                      <p className="lead text-white">
                        An application curated to crisis zones to facilitate
                        dissemination of mission critical information from
                        source to key partners with minimal lag time.
                      </p>
                      <div className="btn-wrapper">
                        <Button
                          className="btn-white btn-icon mb-3 mb-sm-0 ml-1"
                          color="default"
                          href="#responders"
                        >
                          <span className="btn-inner--icon mr-1">
                            <i className="fa fa-ambulance" />
                          </span>
                          <span className="btn-inner--text">
                            For responders
                          </span>
                        </Button>
                      </div>
                    </Col>
                  </Row>
                </div>
              </Container>
              {/* SVG separator */}
            </section>
            {/* 1st Hero Variation */}
          </div>
          <section className="section section-lg" id="responders">
            <Container>
              <Row className="row-grid align-items-center">
                <Col className="order-md-2" md="6">
                  <Form>
                    <Row>
                      <Col md="12">
                        <FormGroup>
                          <Label for="exampleSelect">
                            Select crisis location
                          </Label>
                          <Input type="select" name="location" id="location">
                            <option
                              value="[
                                [-105.301758, 39.964069],
                                [-105.301758, 40.094551],
                                [-105.178142, 40.094551],
                                [-105.178142, 39.964069]
                               ]"
                            >
                              Boulder, Colorado, US
                            </option>
                            <option value="[[-74.259090,40.477398],[-73.700180,40.477398],[-73.700180,40.916178],[-74.259090,40.916178]]">
                              New York City, New York, US
                            </option>
                            <option value="[[-80.319760,25.709051],[-80.139157,25.709051],[-80.139157,25.855782]]">
                              Miami, Florida, US
                            </option>
                            <option value="[[-122.459696,47.481002],[-122.224433,47.481002],[-122.224433,47.734135],[-122.459696,47.734135]]">
                              Seattle, Washington, US
                            </option>
                          </Input>
                        </FormGroup>
                      </Col>
                    </Row>
                    <p>Categories</p>
                    <Row>
                      <Col md="4">
                        <div className="custom-control custom-checkbox mb-3">
                          <input
                            className="custom-control-input"
                            id="bombing"
                            type="checkbox"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor="bombing"
                          >
                            Bombing
                          </label>
                        </div>
                        <div className="custom-control custom-checkbox mb-3">
                          <input
                            className="custom-control-input"
                            id="aid"
                            type="checkbox"
                          />
                          <label className="custom-control-label" htmlFor="aid">
                            Aid
                          </label>
                        </div>
                      </Col>
                      <Col md="4">
                        <div className="custom-control custom-checkbox mb-3">
                          <input
                            className="custom-control-input"
                            id="wildfire"
                            type="checkbox"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor="wildfire"
                          >
                            Wildfire
                          </label>
                        </div>
                        <div className="custom-control custom-checkbox mb-3">
                          <input
                            className="custom-control-input"
                            id="hailstorm"
                            type="checkbox"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor="hailstorm"
                          >
                            Hailstorm
                          </label>
                        </div>
                      </Col>
                      <Col md="4">
                        <div className="custom-control custom-checkbox mb-3">
                          <input
                            className="custom-control-input"
                            id="earthquake"
                            type="checkbox"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor="earthquake"
                          >
                            Earthquake
                          </label>
                        </div>
                        <div className="custom-control custom-checkbox mb-3">
                          <input
                            className="custom-control-input"
                            id="floods"
                            type="checkbox"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor="floods"
                          >
                            Floods
                          </label>
                        </div>
                      </Col>
                    </Row>
                    <Button>Submit</Button>
                  </Form>
                </Col>
                <Col className="order-md-1" md="6">
                  <div className="pr-md-5">
                    <h3>For responders</h3>
                    <p>
                      Fill out the form to get real-time information of crisis
                      areas
                    </p>
                    <ul className="list-unstyled mt-5"></ul>
                  </div>
                </Col>
              </Row>
            </Container>
          </section>
          <section className="section section-lg">
            <Container>
              <Row className="row-grid align-items-center">
                <Col className="order-md-2" md="6">
                  <img
                    alt="..."
                    className="img-fluid floating"
                    src={require("assets/img/crisis.png")}
                  />
                </Col>
                <Col className="order-md-1" md="6">
                  <div className="pr-md-5">
                    <h3>Our mission</h3>
                    <p>
                      Helping individuals get access to accurate information
                      from sources on the ground with little to no lag time.
                    </p>
                    <ul className="list-unstyled mt-5">
                      <li className="py-2">
                        <div className="d-flex align-items-center">
                          <div>
                            <Badge
                              className="badge-circle mr-3"
                              color="success"
                            >
                              <i className="ni ni-check-bold" />
                            </Badge>
                          </div>
                          <div>
                            <h6 className="mb-0">
                              Deliver information about crisis zones with
                              confidence in validity
                            </h6>
                          </div>
                        </div>
                      </li>
                      <li className="py-2">
                        <div className="d-flex align-items-center">
                          <div>
                            <Badge
                              className="badge-circle mr-3"
                              color="success"
                            >
                              <i className="ni ni-check-bold" />
                            </Badge>
                          </div>
                          <div>
                            <h6 className="mb-0">
                              Data visualization to help responders address the
                              crisis
                            </h6>
                          </div>
                        </div>
                      </li>
                      <li className="py-2">
                        <div className="d-flex align-items-center">
                          <div>
                            <Badge
                              className="badge-circle mr-3"
                              color="success"
                            >
                              <i className="ni ni-check-bold" />
                            </Badge>
                          </div>
                          <div>
                            <h6 className="mb-0">
                              Text notifications for users who opt in (coming
                              soon)
                            </h6>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </Col>
              </Row>
            </Container>
          </section>
          <section className="section section-lg">
            <Container>
              <Row className="justify-content-center text-center mb-lg">
                <Col lg="8">
                  <h2 className="display-3">The Codechella Team</h2>
                </Col>
              </Row>
              <Row>
                <Col className="mb-5 mb-lg-0" lg="4" md="8">
                  <div className="px-4">
                    <img
                      alt="..."
                      className="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                      src={require("assets/img/team1.jpg")}
                      style={{ width: "200px" }}
                    />
                    <div className="pt-4 text-center">
                      <h5 className="title">
                        <span className="d-block mb-1">Luisa Escosteguy</span>
                        <small className="h6 text-muted">Web Developer</small>
                      </h5>
                    </div>
                  </div>
                </Col>
                <Col className="mb-5 mb-lg-0" lg="4" md="8">
                  <div className="px-4">
                    <img
                      alt="..."
                      className="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                      src={require("assets/img/team2.jpeg")}
                      style={{ width: "200px" }}
                    />
                    <div className="pt-4 text-center">
                      <h5 className="title">
                        <span className="d-block mb-1">Nandini Talwar</span>
                        <small className="h6 text-muted">Web Developer</small>
                      </h5>
                    </div>
                  </div>
                </Col>
                <Col className="mb-5 mb-lg-0" lg="4" md="8">
                  <div className="px-4">
                    <img
                      alt="..."
                      className="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                      src={require("assets/img/team3.jpg")}
                      style={{ width: "200px" }}
                    />
                    <div className="pt-4 text-center">
                      <h5 className="title">
                        <span className="d-block mb-1">Gobind Bakhshi</span>
                        <small className="h6 text-muted">
                          Backend Developer
                        </small>
                      </h5>
                    </div>
                  </div>
                </Col>
              </Row>
            </Container>
          </section>
        </main>
        <SimpleFooter />
      </>
    );
  }
}

export default Landing;

/**
 * Minified by jsDelivr using Terser v3.14.1.
 * Original file: /npm/react-animate-height@2.0.21/lib/AnimateHeight.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
"use strict";Object.defineProperty(exports,"__esModule",{value:!0});var _typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},_extends=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var i=arguments[e];for(var n in i)Object.prototype.hasOwnProperty.call(i,n)&&(t[n]=i[n])}return t},_createClass=function(){function t(t,e){for(var i=0;i<e.length;i++){var n=e[i];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(t,n.key,n)}}return function(e,i,n){return i&&t(e.prototype,i),n&&t(e,n),e}}(),_react=require("react"),_react2=_interopRequireDefault(_react),_propTypes=require("prop-types"),_propTypes2=_interopRequireDefault(_propTypes),_classnames=require("classnames"),_classnames2=_interopRequireDefault(_classnames);function _interopRequireDefault(t){return t&&t.__esModule?t:{default:t}}function _defineProperty(t,e,i){return e in t?Object.defineProperty(t,e,{value:i,enumerable:!0,configurable:!0,writable:!0}):t[e]=i,t}function _classCallCheck(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function _possibleConstructorReturn(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function _inherits(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}var ANIMATION_STATE_CLASSES={animating:"rah-animating",animatingUp:"rah-animating--up",animatingDown:"rah-animating--down",animatingToHeightZero:"rah-animating--to-height-zero",animatingToHeightAuto:"rah-animating--to-height-auto",animatingToHeightSpecific:"rah-animating--to-height-specific",static:"rah-static",staticHeightZero:"rah-static--height-zero",staticHeightAuto:"rah-static--height-auto",staticHeightSpecific:"rah-static--height-specific"},PROPS_TO_OMIT=["animateOpacity","animationStateClasses","applyInlineTransitions","children","contentClassName","delay","duration","easing","height","onAnimationEnd","onAnimationStart"];function omit(t){for(var e=arguments.length,i=Array(e>1?e-1:0),n=1;n<e;n++)i[n-1]=arguments[n];if(!i.length)return t;for(var a={},o=Object.keys(t),s=0;s<o.length;s++){var r=o[s];-1===i.indexOf(r)&&(a[r]=t[r])}return a}function startAnimationHelper(t){var e=[];return e[0]=requestAnimationFrame(function(){e[1]=requestAnimationFrame(function(){t()})}),e}function cancelAnimationFrames(t){t.forEach(function(t){return cancelAnimationFrame(t)})}function isNumber(t){return!isNaN(parseFloat(t))&&isFinite(t)}function isPercentage(t){return"string"==typeof t&&t.search("%")===t.length-1&&isNumber(t.substr(0,t.length-1))}function runCallback(t,e){t&&"function"==typeof t&&t(e)}var AnimateHeight=function(t){function e(t){_classCallCheck(this,e);var i=_possibleConstructorReturn(this,(e.__proto__||Object.getPrototypeOf(e)).call(this,t));i.animationFrameIDs=[];var n="auto",a="visible";isNumber(t.height)?(n=t.height<0||"0"===t.height?0:t.height,a="hidden"):isPercentage(t.height)&&(n="0%"===t.height?0:t.height,a="hidden"),i.animationStateClasses=_extends({},ANIMATION_STATE_CLASSES,t.animationStateClasses);var o=i.getStaticStateClasses(n);return i.state={animationStateClasses:o,height:n,overflow:a,shouldUseTransitions:!1},i}return _inherits(e,_react2.default.Component),_createClass(e,[{key:"componentDidMount",value:function(){var t=this.state.height;this.contentElement&&this.contentElement.style&&this.hideContent(t)}},{key:"componentDidUpdate",value:function(t,e){var i=this,n=this.props,a=n.delay,o=n.duration,s=n.height,r=n.onAnimationEnd,l=n.onAnimationStart;if(this.contentElement&&s!==t.height){var h;this.showContent(e.height),this.contentElement.style.overflow="hidden";var u=this.contentElement.offsetHeight;this.contentElement.style.overflow="";var c=o+a,p=null,m={height:null,overflow:"hidden"},f="auto"===e.height;isNumber(s)?(p=s<0||"0"===s?0:s,m.height=p):isPercentage(s)?(p="0%"===s?0:s,m.height=p):(p=u,m.height="auto",m.overflow=null),f&&(m.height=p,p=u);var g=(0,_classnames2.default)((_defineProperty(h={},this.animationStateClasses.animating,!0),_defineProperty(h,this.animationStateClasses.animatingUp,"auto"===t.height||s<t.height),_defineProperty(h,this.animationStateClasses.animatingDown,"auto"===s||s>t.height),_defineProperty(h,this.animationStateClasses.animatingToHeightZero,0===m.height),_defineProperty(h,this.animationStateClasses.animatingToHeightAuto,"auto"===m.height),_defineProperty(h,this.animationStateClasses.animatingToHeightSpecific,m.height>0),h)),y=this.getStaticStateClasses(m.height);this.setState({animationStateClasses:g,height:p,overflow:"hidden",shouldUseTransitions:!f}),clearTimeout(this.timeoutID),clearTimeout(this.animationClassesTimeoutID),f?(m.shouldUseTransitions=!0,cancelAnimationFrames(this.animationFrameIDs),this.animationFrameIDs=startAnimationHelper(function(){i.setState(m),runCallback(l,{newHeight:m.height})}),this.animationClassesTimeoutID=setTimeout(function(){i.setState({animationStateClasses:y,shouldUseTransitions:!1}),i.hideContent(m.height),runCallback(r,{newHeight:m.height})},c)):(runCallback(l,{newHeight:p}),this.timeoutID=setTimeout(function(){m.animationStateClasses=y,m.shouldUseTransitions=!1,i.setState(m),"auto"!==s&&i.hideContent(p),runCallback(r,{newHeight:p})},c))}}},{key:"componentWillUnmount",value:function(){cancelAnimationFrames(this.animationFrameIDs),clearTimeout(this.timeoutID),clearTimeout(this.animationClassesTimeoutID),this.timeoutID=null,this.animationClassesTimeoutID=null,this.animationStateClasses=null}},{key:"showContent",value:function(t){0===t&&(this.contentElement.style.display="")}},{key:"hideContent",value:function(t){0===t&&(this.contentElement.style.display="none")}},{key:"getStaticStateClasses",value:function(t){var e;return(0,_classnames2.default)((_defineProperty(e={},this.animationStateClasses.static,!0),_defineProperty(e,this.animationStateClasses.staticHeightZero,0===t),_defineProperty(e,this.animationStateClasses.staticHeightSpecific,t>0),_defineProperty(e,this.animationStateClasses.staticHeightAuto,"auto"===t),e))}},{key:"render",value:function(){var t,e=this,i=this.props,n=i.animateOpacity,a=i.applyInlineTransitions,o=i.children,s=i.className,r=i.contentClassName,l=i.duration,h=i.easing,u=i.delay,c=i.style,p=this.state,m=p.height,f=p.overflow,g=p.animationStateClasses,y=p.shouldUseTransitions,d=_extends({},c,{height:m,overflow:f||c.overflow});y&&a&&(d.transition="height "+l+"ms "+h+" "+u+"ms",c.transition&&(d.transition=c.transition+", "+d.transition),d.WebkitTransition=d.transition);var _={};n&&(_.transition="opacity "+l+"ms "+h+" "+u+"ms",_.WebkitTransition=_.transition,0===m&&(_.opacity=0));var T=(0,_classnames2.default)((_defineProperty(t={},g,!0),_defineProperty(t,s,s),t));return _react2.default.createElement("div",_extends({},omit.apply(void 0,[this.props].concat(PROPS_TO_OMIT)),{"aria-hidden":0===m,className:T,style:d}),_react2.default.createElement("div",{className:r,style:_,ref:function(t){return e.contentElement=t}},o))}}]),e}(),heightPropType=function(t,e,i){var n=t[e];return"number"==typeof n&&n>=0||isPercentage(n)||"auto"===n?null:new TypeError('value "'+n+'" of type "'+(void 0===n?"undefined":_typeof(n))+'" is invalid type for '+e+" in "+i+'. It needs to be a positive number, string "auto" or percentage string (e.g. "15%").')};AnimateHeight.propTypes={animateOpacity:_propTypes2.default.bool,animationStateClasses:_propTypes2.default.object,applyInlineTransitions:_propTypes2.default.bool,children:_propTypes2.default.any.isRequired,className:_propTypes2.default.string,contentClassName:_propTypes2.default.string,duration:_propTypes2.default.number,delay:_propTypes2.default.number,easing:_propTypes2.default.string,height:heightPropType,onAnimationEnd:_propTypes2.default.func,onAnimationStart:_propTypes2.default.func,style:_propTypes2.default.object},AnimateHeight.defaultProps={animateOpacity:!1,animationStateClasses:ANIMATION_STATE_CLASSES,applyInlineTransitions:!0,duration:250,delay:0,easing:"ease",style:{}},exports.default=AnimateHeight;
//# sourceMappingURL=/sm/71accf86f00c217838397b5b63b8af81eff752fc6df1d29f2c91a577fe9cd55e.map
odoo.define('bicicletario.bicicletario', function (require) {
    'use strict';

    var core = require('web.core');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;

    var BicicletarioWidget = Widget.extend({
        template: 'bicicletario.index',
        xmlDependencies: ['/bicicletario/static/src/xml/index.xml'],

        start: function () {
            return this._super.apply(this, arguments);
        },
    });

    core.action_registry.add('bicicletario.action', BicicletarioWidget);

    return Bic

'use strict';
const InfoBot = require('./modules/infobot.js');
require('dotenv').config();
const { exit } = require('process');

const config = require ('../config.json');


const CommandoClient = new InfoBot({
    owner: config.ids.owner,
    commandPrefix: config.prefix,
});


// log in
if (process.argv.length < 2) {
    console.log('Please specify an application [H/T]');
    exit(1);
}
else if (process.argv[2] == 'I') {
    console.log('Logging in as informatik.bot');
    CommandoClient.login(process.env.INFOBOT_TOKEN);
}
else if (process.argv[2] == 'T') {
    console.log('Logging in as Chester McTester');
    CommandoClient.login(process.env.TESTBOT_TOKEN);
}
else {
    console.log(`Invalid app provided. [${process.argv[2]}`);
    exit(1);
}

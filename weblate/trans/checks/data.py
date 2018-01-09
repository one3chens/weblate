# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2017 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from __future__ import unicode_literals

# We ignore some words which are usually not translated
SAME_BLACKLIST = frozenset((
    'abc',
    'accelerator',
    'account',
    'action',
    'actions',
    'active',
    'add-ons',
    'addons',
    'address',
    'admin',
    'administrator',
    'administration',
    'africa',
    'agenda',
    'alarm',
    'album',
    'alias',
    'aliases',
    'aliasing',
    'alt',
    'altitude',
    'amazon',
    'android',
    'antialias',
    'antialiasing',
    'api',
    'applet',
    'appliance',
    'appliances',
    'aptitude',
    'area',
    'array',
    'artist',
    'attribute',
    'attribution',
    'atom',
    'audio',
    'author',
    'auto',
    'autostart',
    'authentication',
    'avatar',
    'backend',
    'backspace',
    'backup',
    'badge',
    'balance',
    'baltic',
    'bank',
    'bar',
    'baseball',
    'battery',
    'begin',
    'bios',
    'bit',
    'bitcoin',
    'bitcoins',
    'bitmap',
    'bitmaps',
    'bitrate',
    'block',
    'blog',
    'bluetooth',
    'bool',
    'boolean',
    'boot',
    'bootloader',
    'branch',
    'broadcast',
    'browser',
    'buffer',
    'byte',
    'bytes',
    'bzip',
    'bzip2',
    'cable',
    'cache',
    'captcha',
    'caps',
    'cardinality',
    'charset',
    'charsets',
    'chat',
    'china',
    'click',
    'client',
    'clipboard',
    'club',
    'code',
    'collation',
    'color',
    'command',
    'commit',
    'component',
    'components',
    'compression',
    'conductor',
    'configuration',
    'console',
    'contact',
    'contacts',
    'context',
    'control',
    'cookie',
    'cookies',
    'copyright',
    'creation',
    'criteria',
    'crypt',
    'csd',
    'csv',
    'ctrl',
    'cvs',
    'cyrillic',
    'dashboard',
    'data',
    'database',
    'databases',
    'date',
    'datum',
    'dbm',
    'debian',
    'debug',
    'default',
    'definition',
    'del',
    'delete',
    'demo',
    'description',
    'design',
    'designer',
    'destination',
    'detail',
    'details',
    'developer',
    'devscripts',
    'dialog',
    'ding',
    'direction',
    'disc',
    'distance',
    'distribution',
    'distro',
    'dns',
    'doc',
    'docs',
    'doctor',
    'document',
    'documentation',
    'dollar',
    'download',
    'downloads',
    'dpkg',
    'dpi',
    'drizzle',
    'dummy',
    'dump',
    'e-mail',
    'editor',
    'eib',
    'ellipsis',
    'email',
    'end',
    'engine',
    'engines',
    'enter',
    'enterprise',
    'enum',
    'error',
    'escape',
    'ethernet',
    'exchange',
    'excel',
    'expert',
    'explore',
    'export',
    'expression',
    'extension',
    'extra',
    'extras',
    'event',
    'events',
    'false',
    'fame',
    'fanfare',
    'farm',
    'fauna',
    'fax',
    'fedora',
    'feeds',
    'feet',
    'file',
    'files',
    'filter',
    'filters',
    'finance',
    'finalisation',
    'fingerprint',
    'firewall',
    'firmware',
    'fjord',
    'flash',
    'flattr',
    'flora',
    'font',
    'format',
    'forum',
    'freemind',
    'freeplane',
    'frequency',
    'full',
    'fulltext',
    'function',
    'gammu',
    'gas',
    'general',
    'genre',
    'gentoo',
    'geocache',
    'geocaching',
    'gettext',
    'global',
    'gnu',
    'golf',
    'google',
    'gib',
    'git',
    'gpl',
    'gps',
    'gpx',
    'graphic',
    'graphics',
    'grant',
    'gtk',
    'gzip',
    'hack',
    'hacks',
    'hall',
    'handle',
    'handler',
    'hardware',
    'hash',
    'hashed',
    'headset',
    'help',
    'hmpf',
    'home',
    'homepage',
    'hong',
    'hook',
    'horizontal',
    'host',
    'hosting',
    'hostname',
    'hostel',
    'hotel',
    'html',
    'http',
    'https',
    'hut',
    'hybrid',
    'hyperlink',
    'iban',
    'icmp',
    'icon',
    'icons',
    'ids',
    'idea',
    'ignore',
    'irc',
    'irda',
    'illustration',
    'image',
    'imap',
    'imei',
    'imsi',
    'import',
    'inconsistent',
    'index',
    'india',
    'indigo',
    'individual',
    'info',
    'information',
    'infrastructure',
    'inline',
    'innodb',
    'input',
    'ins',
    'insert',
    'install',
    'installation',
    'int',
    'integer',
    'interlingua',
    'internet',
    'international',
    'intro',
    'introduction',
    'ion',
    'ios',
    'ip6tables',
    'iptables',
    'ipv4',
    'ipv6',
    'irix',
    'isbn',
    'ismn',
    'issn',
    'isrc',
    'item',
    'items',
    'jabber',
    'java',
    'join',
    'joins',
    'jpeg',
    'jpg',
    'karaoke',
    'kernel',
    'kib',
    'kill',
    'knoppix',
    'kong',
    'korfbal',
    'label',
    'labels',
    'land',
    'latex',
    'latin',
    'latitude',
    'layout',
    'ldif',
    'leap',
    'level',
    'libgammu',
    'linestring',
    'link',
    'links',
    'linux',
    'list',
    'litecoin',
    'lithium',
    'lock',
    'local',
    'locales',
    'log',
    'logcheck',
    'login',
    'logo',
    'logos',
    'longitude',
    'lord',
    'ltr',
    'lua',
    'lzma',
    'magazine',
    'magazines',
    'magenta',
    'mah',
    'manager',
    'mandrake',
    'mandriva',
    'manual',
    'mail',
    'mailbox',
    'mailboxes',
    'maildir',
    'mailing',
    'mako',
    'markdown',
    'master',
    'max',
    'maximum',
    'media',
    'mediawiki',
    'menu',
    'merge',
    'mesh',
    'message',
    'messages',
    'meta',
    'metadata',
    'metal',
    'metre',
    'metres',
    'mib',
    'micropayment',
    'micropayments',
    'microsoft',
    'migration',
    'mile',
    'min',
    'minimum',
    'mint',
    'minus',
    'minute',
    'minutes',
    'mode',
    'model',
    'module',
    'modules',
    'monitor',
    'mono',
    'monument',
    'motel',
    'motif',
    'mouse',
    'mph',
    'mysql',
    'multiplayer',
    'musicbottle',
    'name',
    'namecoin',
    'namecoins',
    'navigation',
    'net',
    'netfilter',
    'network',
    'neutral',
    'nimh',
    'node',
    'none',
    'normal',
    'note',
    'notes',
    'notify',
    'notification',
    'null',
    'num',
    'number',
    'numeric',
    'obex',
    'office',
    'offline',
    'ogg',
    'online',
    'opac',
    'open',
    'opendocument',
    'openmaps',
    'openpgp',
    'openstreet',
    'opensuse',
    'openvpn',
    'opera',
    'operator',
    'option',
    'options',
    'orange',
    'orientation',
    'osm',
    'osmand',
    'output',
    'overhead',
    'package',
    'page',
    'pager',
    'pages',
    'parameter',
    'parameters',
    'park',
    'parking',
    'partition',
    'partitions',
    'parser',
    'party',
    'password',
    'pause',
    'paypal',
    'pdf',
    'pdu',
    'percent',
    'perfume',
    'personal',
    'performance',
    'php',
    'phpmyadmin',
    'pib',
    'picasa',
    'ping',
    'pirate',
    'pirates',
    'pixel',
    'pixels',
    'placement',
    'plan',
    'playlist',
    'plugin',
    'plugins',
    'plural',
    'plus',
    'png',
    'podcast',
    'podcasts',
    'point',
    'polygon',
    'polymer',
    'pool',
    'port',
    'portable',
    'portrait',
    'position',
    'post',
    'postgresql',
    'posts',
    'pre',
    'pre-commit',
    'prefix',
    'prince',
    'privacy',
    'private',
    'procedure',
    'procedures',
    'process',
    'profiling',
    'program',
    'project',
    'promotion',
    'property',
    'properties',
    'protocol',
    'provider',
    'proxy',
    'pull',
    'push',
    'python',
    'python-gammu',
    'query',
    'question',
    'questions',
    'radar',
    'radio',
    'radius',
    'rate',
    'realm',
    'rebase',
    'redhat',
    'regexp',
    'region',
    'relation',
    'relations',
    'render',
    'replication',
    'repository',
    'report',
    'reports',
    'reset',
    'resource',
    'responsive',
    'restaurant',
    'restaurants',
    'return',
    'rich-text',
    'richtext',
    'roadmap',
    'robot',
    'role',
    'root',
    'route',
    'routine',
    'routines',
    'rss',
    'rst',
    'rtl',
    'salt',
    'sauna',
    'saver',
    'scalable',
    'scenario',
    'score',
    'screen',
    'screenshot',
    'screensaver',
    'script',
    'scripts',
    'scripting',
    'scroll',
    'sdk',
    'sector',
    'seed',
    'selinux',
    'send',
    'sergeant',
    'serie',
    'series',
    'server',
    'servers',
    'service',
    'set',
    'shell',
    'shift',
    'sim',
    'singular',
    'site',
    'skype',
    'slash',
    'slide',
    'slideshow',
    'slot',
    'slots',
    'slug',
    'sms',
    'smsc',
    'smsd',
    'snapshot',
    'snapshots',
    'snmp',
    'socket',
    'software',
    'solaris',
    'source',
    'spatial',
    'spline',
    'sponsor',
    'sponsors',
    'sport',
    'sql',
    'sqlite',
    'standard',
    'start',
    'stat',
    'statement',
    'stats',
    'status',
    'stereo',
    'stop',
    'string',
    'strings',
    'structure',
    'style',
    'submit',
    'subproject',
    'subquery',
    'substring',
    'suggestion',
    'suggestions',
    'sum',
    'sunos',
    'supermarket',
    'support',
    'surfing',
    'suse',
    'svg',
    'symbol',
    'synaptic',
    'syndication',
    'system',
    'swap',
    'tab',
    'table',
    'tables',
    'tabs',
    'tada',
    'tag',
    'tags',
    'taiwan',
    'taxi',
    'taxon',
    'tbx',
    'team',
    'teams',
    'technology',
    'telnet',
    'template',
    'tent',
    'term',
    'termbase',
    'test',
    'texy',
    'text',
    'theme',
    'theora',
    'thread',
    'threads',
    'tib',
    'timer',
    'tip',
    'todo',
    'todos',
    'total',
    'transfer',
    'transformation',
    'transformations',
    'transport',
    'tray',
    'trigger',
    'triggers',
    'true',
    'tutorial',
    'tour',
    'type',
    'twiki',
    'twitter',
    'ubuntu',
    'uefi',
    'ukolovnik',
    'unicode',
    'unique',
    'unit',
    'universal',
    'unix',
    'update',
    'upload',
    'url',
    'utf',
    'variable',
    'variables',
    'vcalendar',
    'vcard',
    'vector',
    'vendor',
    'version',
    'versions',
    'vertical',
    'video',
    'view',
    'views',
    'virus',
    'vorbis',
    'vote',
    'votes',
    'wammu',
    'web',
    'weblate',
    'webmail',
    'website',
    'widget',
    'widgets',
    'wifi',
    'wiki',
    'wikipedia',
    'wildcard',
    'windowed',
    'windows',
    'word',
    'www',
    'xen',
    'xhtml',
    'xkeys',
    'xml',
    'yard',
    'zen',
    'zero',
    'zip',
    'zombie',
    'zone',
    'zoo',
    'zoom',

    # Currencies
    'btc',
    'eur',
    'usd',

    # Months are same in some languages
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december',

    'jan',
    'feb',
    'mar',
    'apr',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec',

    # Week names shotrcuts
    'mon',
    'tue',
    'wed',
    'thu',
    'fri',
    'sat',
    'sun',

    # Roman numbers
    'iii',

    # Architectures
    'alpha',
    'amd',
    'amd64',
    'arm',
    'aarch',
    'aarch64',
    'hppa',
    'i386',
    'i586',
    'm68k',
    'powerpc',
    'sparc',
    'x86_64',

    # whole alphabet
    'abcdefghijklmnopqrstuvwxyz',
))

import ConfigParser, os, argparse

def main():
    parser = argparse.ArgumentParser(description='change default profile in aws credentials file.')
    parser.add_argument('profile', help='Profile name')
    parser.add_argument('-c', '--credentials', dest='credentials', 
                        help='AWS credentials', required=False, default="~/.aws/credentials")
    args = parser.parse_args()
    config = ConfigParser.ConfigParser()

    if not os.path.isfile(os.path.expanduser(args.credentials)):
        print "credentials file not found. check your aws credentials file (~/.aws/credentials)."
        return 1

    bkp_section = 'aws-default-previously'
    default_section = 'default'
    config.read(os.path.expanduser(args.credentials))
    try:
        items = config.items(default_section)
        if not config.has_section(bkp_section):
            config.add_section(bkp_section)
        for item in items:
            config.set(bkp_section, item[0], item[1])

        items = config.items(args.profile)
        for item in items:
            config.set(default_section, item[0], item[1])

        cfgfile = open(os.path.expanduser(args.credentials), 'w')
        config.write(cfgfile)
        return 0
    except Exception, e:
        print e
        return 1
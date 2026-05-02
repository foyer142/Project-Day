import storage,api_client, report



def main()-> None:
    users = storage.load_users('day14/user.json')
    github_info = api_client.get_github_status()
    report_file = report.build_report(users,github_info)
    print(report_file)

if __name__ == '__main__':
    main()
    
export default function Layout({
  private: Private,
  public: Public,
}: {
  private: React.ReactNode;
  public: React.ReactNode;
}) {
  const isAuthenticated = true;
  return <div>{isAuthenticated ? Private : Public}</div>;
}
